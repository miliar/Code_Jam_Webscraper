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

LL GetMin(LL n, LL p) {
    if (p == (1LL << n) - 1) {
        return p;
    }
    LL cur = 0;
    LL pos = 0;
    LL shift = 1LL << (n-1);
    LL cnt = 2;
    while (pos + shift <= p) {
        pos += shift;
        shift /= 2;
        cur += cnt;
        cnt *= 2;
    }
    return cur;
}

LL GetMax(LL n, LL p) {
    LL how = 0;
    LL curpos = 1LL << n;
    while (p < curpos - 1) {
        ++how;
        curpos /= 2;
    }
    LL cur = (1LL << n) - 1;
    LL shift = 1;
    for (int i = 0; i < how; ++i) {
        cur -= shift;
        shift *= 2;
    }
    return cur;
}

void Solution() {
    LL n, p;
    cin >> n >> p;
    --p;
    cout << GetMin(n, p) << " " << GetMax(n, p) << endl;
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
