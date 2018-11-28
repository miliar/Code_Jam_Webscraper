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
int firstD[SZ][SZ];
int secondD[SZ][SZ];
int first, second;
vector <int> maybeFirst;
vector <int> maybeSecond;

void getData() {
	cin >> first;
	--first;
	for (int i = 0; i < 4; ++i) {
		for (int j = 0; j < 4; ++j) {
			cin >> firstD[i][j];
		}
	}
	cin >> second;
	--second;
	for (int i = 0; i < 4; ++i) {
		for (int j = 0; j < 4; ++j) {
			cin >> secondD[i][j];
		}
	}
}

string getAns() {
	string ans = "";
	for (int i = 0; i < 4; ++i) {
		maybeFirst.ppb(firstD[first][i]);
		maybeSecond.ppb(secondD[second][i]);
	}

	int num = -1;
	int cnt = 0;

	for (int i = 0; i < 4; ++i) {
		for (int j = 0; j < 4; ++j) {
			if (maybeFirst[i] == maybeSecond[j]) {
				num = maybeFirst[i];
				++cnt;
			}
		}
	}

	if (cnt == 1) {
		return to_string(num);
	}

	if (cnt == 0) {
		return "Volunteer cheated!";
	}

	return "Bad magician!";
}

void clear() {
	for (int i = 0; i < SZ; ++i) {
		for (int j = 0; j < SZ; ++j) {
			firstD[i][j] = 0;
			secondD[i][j] = 0;
		}
	}
	maybeFirst.clear();
	maybeSecond.clear();
}

void solve() {
	cin >> t;
	for (int i = 0; i < t; ++i) {
		clear();
		getData();
		string ans = getAns();
		cout << "Case #" << i + 1 << ": " << ans << endl;
	}
}

int main() {

prepare("A");

ios::sync_with_stdio(false);

//startTimer();

	//getData();
	solve();

//stopTimer();
	return 0;
}