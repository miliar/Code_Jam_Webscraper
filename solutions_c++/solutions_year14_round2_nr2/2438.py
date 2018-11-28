//C++ Template: http://pastebin.com/dGrr0CpX
 
#pragma comment(linker,"/STACK:256000000")
#define _CRT_SECURE_NO_WARNINGS
 
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
#define sqr(x) ((x)*(x))
#define ppb push_back
#define mp make_pair
 
const int SZ = 1100;
const int INF = 1000*1000*1000;
const double inf = 1e9;
const double eps = 1e-7;
 
double start, finish;
/****************************************************************************/
void prepare(string s) {
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
#else
    if (sz(s) != 0) {
        if (s == "ACMP") {
            freopen("INPUT.TXT", "r", stdin);
            freopen("OUTPUT.TXT", "w", stdout);
        } else {
            freopen((s + ".in").c_str(), "r", stdin);
            freopen((s + ".out").c_str(), "w", stdout);
        }
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

int test;

void solve() {
	cin >> test;
	for (int t = 1; t <= test; ++t) {
		int a, b, k;
		cin >> a >> b >> k;
		int cnt = 0;
		for (int i = 0; i < a; ++i) {
			for (int j = 0; j < b; ++j) {
				if ((i & j) < k) {
					//cout << i << " " << j << endl;
					++cnt;
				}
			}
		}
		cout << "Case #" << t << ": " << cnt << endl;
	}
}

int main() {
 
prepare("B");
 
ios::sync_with_stdio(false);
 
startTimer();
 
    //getData();
    solve();
 
stopTimer();
    return 0;
}