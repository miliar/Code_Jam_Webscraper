#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <cstdio>
#include <ctime>
#include <utility>
#include <iomanip>

using namespace std;

typedef long long LL;
template<typename T> inline T Abs(const T& x) { return x < 0 ? -x : x; }
template<typename T> inline T Sqr(const T& x) { return x * x; }

int N;
bool flag;

bool Try(vector<int> cur, const vector<int>& a, const vector<int>& b, int from) {
    if (from == N+1) {
        for (int i = 0; i < cur.size(); ++i) {
            cout << cur[i] << (i+1 < cur.size() ? " " : "");
        }
        cout << endl;
        flag = false;
        return true;
    }
    vector<int> mx(N, 0), mn(N, 0);
    for (int j = 0; j < N; ++j) {
        mx[j] = 1;
        for (int k = 0; k < j; ++k) {
            if (cur[k] && (cur[j] == 0 || cur[j] > cur[k]) && mx[k] + 1 > mx[j]) {
                mx[j] = mx[k] + 1;
            }
        }
    }
    for (int j = N-1; j >= 0; --j) {
        mn[j] = 1;
        for (int k = j+1; k < N; ++k) {
            if (cur[k] && (cur[j] == 0 || cur[j] > cur[k]) && mn[k] + 1 > mn[j]) {
                mn[j] = mn[k] + 1;
            }
        }
    }
    for (int j = 0; j < N; ++j) {
        if (flag == false) {
            return false;
        }
        if (a[j] == mx[j] && b[j] == mn[j] && cur[j] == 0) {
            cur[j] = from;
            if (Try(cur, a, b, from + 1)) {
                return true;
            }
            
            cur[j] = 0;
        }
    }
    return false;
}

void Solution() {
    int n;
    cin >> n;
    flag = true;
    N = n;
    vector<int> a(n), b(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    for (int i = 0; i < n; ++i) {
        cin >> b[i];
    }
    
    vector<int> cur(n, 0);
    for (int i = 0; i < n; ++i) {
        if (a[i] == 1 && b[i] == 1) {
            cur[i] = 1;
            Try(cur, a, b, 2);
        }
    }
}


struct Timer {
    map<string, float> starts;
    void Tic(const string& name) { starts[name] = clock(); }
    float Toc(const string& name) { return (clock() - starts[name]) / CLOCKS_PER_SEC; }
} timer;

int main(int argc, char* argv[]) {
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

    timer.Tic("global");
    int testsNumber;
    cin >> testsNumber;
    for (int curTest = 1; curTest <= testsNumber; ++curTest) {
        cout << "Case #" << curTest << ": ";
        cerr << "Case #" << setw(2) << setfill('0') << curTest << ": running...";
        timer.Tic("test");
        Solution();
        cerr << "done! Elapsed time is " << setprecision(3) << timer.Toc("test") << endl;
    }
    cerr << endl << "Total elapsed time is " << setprecision(3) << timer.Toc("global") << endl;

    return 0;
}
