#pragma comment(linker,"/STACK:268435456")

#include <algorithm>
#include <iostream>
#include <memory.h>
#include <iomanip>
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
#include <queue>
#include <ctime>
#include <set>
#include <map>

using namespace std;

#define all(a) a.begin(), a.end()
#define PI 3.14159265358979
#define sz(a) (int)a.size()
#define ppb push_back
#define mp make_pair

template <class T> T sqr(T n) {
    return n*n;
}

template <class T> T gcd(T a, T b) {
    while (b) {
        a %= b;
        cout << a << " " << b << endl;
        swap(a, b);
    }
    return a;
}

const int SZ = 510;
const int INF = 1000*1000*1000;

double start, finish;
/****************************************************************************/
void startTimer() {
#ifdef _DEBUG
    start = clock();
#endif
}

void stopTimer() {
#ifdef _DEBUG
    finish = clock();
    cout << "\n*** Total time ***\n" << (finish - start)/CLOCKS_PER_SEC << endl;
#endif
}
/****************************************************************************/

int tests;
string s;
int n;
set <char> ch;

int getNum(string t) {
    int cnt = 0, m = 0;
    for (int i = 0; i < sz(t); ++i) {
        if (ch.find(t[i]) == ch.end()) {
            ++cnt;
        } else {
            cnt = 0;
        }
        m = max(m, cnt);
    }
    return m;
}

void getData() {
    cin >> tests;
    string t = "aeiou";
    for (int i = 0; i < sz(t); ++i) {
        ch.insert(t[i]);
    }
}

void solve() {
    for (int tsts = 0; tsts < tests; ++tsts) {
        cin >> s >> n;
        int cnt = 0, ans = 0;
        for (int i = 0; i < sz(s); ++i) {
            for (int j = 1; j <= sz(s) - i; ++j) {
                string tmp = s.substr(i, j);
                cnt = 0;
                cnt = getNum(tmp);
                if (cnt >= n) {
                    ++ans;
                }
            }
        }
        cout << "Case #" << tsts + 1 << ": " << ans << endl;
    }
}

int main() {

ios::sync_with_stdio(false);    
freopen("A.in", "r", stdin);   
freopen("output.txt", "w", stdout);

startTimer();

    getData();
    solve();

stopTimer();
    return 0;
}