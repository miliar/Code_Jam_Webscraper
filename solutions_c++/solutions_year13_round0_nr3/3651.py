//C++ Template: http://pastebin.com/dGrr0CpX

#pragma comment(linker,"/STACK:256000000")

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
#define sec second
#define fis first

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

const int SZ = 1010;
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

int n;
string a, b;
long long d[] = {1, 2, 3, 11, 22, 111, 121, 1111, 11111, 11211, 111111, 1111111, 11111111, 111111111, 1111111111};
vector <long long> sqrs;

int main() {

prepare("");
ios::sync_with_stdio(false);

startTimer();

	freopen("problemC.txt", "w", stdout);
	for (int i = 0; i < 15; ++i) {
		sqrs.ppb(sqr(d[i]));
	}
	cin >> n;
	for (int z = 0; z < n; ++z) {
		cin >> a >> b;
		int cnt = 0;
		long long Ia = -1, Ib = -1;
		if (sz(a) <= 10) {
			Ia = atoi(a.c_str());
		}
		if (sz(b) <= 10) {
			Ib = atoi(b.c_str());
		}
		if (Ia != -1) {
			if (Ib == -1) {
				Ib = 12345678900987654321;
			}
			for (int i = 0; i < 14; ++i) {
				if (sqrs[i] >= Ia && sqrs[i] <= Ib) {
					++cnt;
				}
			}
		}
		cout << "Case #" << z + 1 << ": " << cnt << endl;
	}

stopTimer();
	return 0;
}