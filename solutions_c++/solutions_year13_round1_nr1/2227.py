//C++ Template: http://pastebin.com/dGrr0CpX

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

#define _DEBUG

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
void prepare(string s) {
#ifdef _DEBUG
    freopen("input.txt", "r", stdin);
#else
    if (sz(s) != 0) {
        freopen((s + ".in").c_str(), "r", stdin);
        freopen((s + ".out").c_str(), "w", stdout);
    }
#endif
}

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

const double Pi = 3.1415926535;

int tests;
long long t, r;


void getData() {
	cin >> tests;
}

void solve() {
	for (int i = 0; i < tests; ++i) {
		cin >> r >> t;
		long long cnt = 0, curr_r = r + 1;
		while (1) {
			t -= (sqr(curr_r) - sqr(r));	
			if (t < 0) {
				break;
			}
			curr_r += 2; r += 2; 		
			++cnt;
		}
		cout << "Case #" << i + 1 << ": " << cnt << endl;
	}
}

int main() {

//prepare("");
ios::sync_with_stdio(false);    

startTimer();

	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
    getData();
    solve();

stopTimer();
    return 0;
}