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

const int SZ = 5;
const int INF = 1000*1000*1000;
const double inf = 1e9;
const double eps = 1e-5;

double start, finish;
/****************************************************************************/
void prepare(string s) {
#ifdef _DEBUG
	if (sz(s) != 0) {
		freopen((s + ".in").c_str(), "r", stdin);
	} else {
		freopen("input.txt", "r", stdin);
	}
	freopen("output.txt", "w", stdout);
#else
	if (sz(s) != 0) {
		freopen((s + ".in").c_str(), "r", stdin);
	//	freopen((s + ".out").c_str(), "w", stdout);
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

int t;
double c, f, x;

void getData() {
	cin >> c >> f >> x;
}

double getAns() {
	double rate = 2.0;
	double sumTime = 0.0;
	while (1) {
		double justClick = x / rate;
		double withFarm = c / rate + x / (rate + f);
		if (withFarm >= justClick) {
			return sumTime + justClick;
		}
		sumTime += c / rate;
		rate += f;
	}
}

void solve() {
	cin >> t;
	for (int i = 0; i < t; ++i) {
		getData();
		double ans = getAns();
		cout << "Case #" << i + 1 << ": ";
		cout << fixed << setprecision(7) << ans << endl;
	}
}

int main() {

prepare("B");

ios::sync_with_stdio(false);

//startTimer();

	//getData();
	solve();

//stopTimer();
	return 0;
}