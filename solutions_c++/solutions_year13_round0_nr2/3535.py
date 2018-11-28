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


void Solution() {
    int n, m;
    cin >> n >> m;
    vector<int> row(n, 1), col(m, 1);
    vector< vector<int> > a(n, vector<int>(m, 0));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> a[i][j];
            row[i] = max(row[i], a[i][j]);
            col[j] = max(col[j], a[i][j]);
        }
    }
    bool yes = true;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (a[i][j] < col[j] && a[i][j] < row[i]) {
                yes = false;
            }
        }
    }
    cout << (yes ? "YES": "NO") << endl;
}


struct Timer {
    map<string, float> starts;
    void Tic(const string& name) { starts[name] = clock(); }
    float Toc(const string& name) { return (clock() - starts[name]) / CLOCKS_PER_SEC; }
} timer;

int main(int argc, char* argv[]) {
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

    ios_base::sync_with_stdio(false);

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
