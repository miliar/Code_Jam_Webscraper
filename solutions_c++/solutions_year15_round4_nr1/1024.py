#include <bits/stdc++.h>

#define pb push_back
#define mp make_pair
#define all(x) (x).begin(), (x).end()
#define x first
#define y second

using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef int itn;
typedef pair<int, int> PII;

struct InputData {
    int n, m;
    vector<string> a;
};

struct OutputData {
    string ans;
    void print();
};

InputData readInputData();
OutputData solve(InputData);

int main() {
    freopen( "input.txt", "r", stdin );
    freopen("output.txt", "w", stdout);

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    srand(3242322);

    ld cl0 = clock();

    int t;
    cin >> t;
    future<OutputData> fu[t];

    cerr << "Reading input..." << endl;
    for (int i = 0; i < t; ++i) {
        InputData inputData = readInputData();
        fu[i] = async(launch::async, solve, inputData);
    }

    OutputData res[t];
    cerr << "Waiting for threads..." << endl;
    for (int i = 0; i < t; ++i) {
        res[i] = fu[i].get();
    }


    cerr << "Printing results..." << endl;
    for (int i = 0; i < t; ++i) {
        cout << "Case #" << i + 1 << ": ";
        res[i].print();
        cout << endl;
    }


    cerr << setprecision(3) << fixed;
    cerr << "Time: " << (clock() - cl0) / (CLOCKS_PER_SEC) << " sec." << endl;
    return 0;
}


pair<int, int> dir(char c) {
    if (c == 'v') {
        return mp(1, 0);
    }
    if (c == '>') {
        return mp(0, 1);
    }
    if (c == '<') {
        return mp(0, -1);
    }
    if (c == '^') {
        return mp(-1, 0);
    }
    return mp(0, 0);
}

OutputData solve(InputData in) {
    OutputData out;


    int ans = 0;
    int n = in.n;
    int m = in.m;
    vector<string> s = in.a;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (s[i][j] != '.') {
                int cnt1 = 0;
                for (int k = 0; k < n; ++k) {
                    if (s[k][j] != '.') {
                        ++cnt1;
                    }
                }
                int cnt2 = 0;
                for (int k = 0; k < m; ++k) {
                    if (s[i][k] != '.') {
                        ++cnt2;
                    }
                }
                if (cnt1 == 1 && cnt2 == 1) {
                    out.ans = "IMPOSSIBLE";
                    return out;
                }
            }
        }
    }

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (s[i][j] != '.') {
                PII d = dir(s[i][j]);
                for (int k = 1;; ++k) {
                    PII v;
                    v.x = i + d.x * k;
                    v.y = j + d.y * k;
                    if (v.x < 0 || v.y < 0 || v.x >= n || v.y >= m) {
                        ++ans;
                        break;
                    }
                    if (s[v.x][v.y] != '.') {
                        break;
                    }
                }
            }
        }
    }
    out.ans = to_string(ans);
    return out;
}

InputData readInputData() {
    InputData inp;
    cin >> inp.n >> inp.m;
    inp.a.resize(inp.n);
    for (int i = 0; i < inp.n; ++i) {
        cin >> inp.a[i];
    }
    return inp;
}

void OutputData::print() {
    cout << ans;
}