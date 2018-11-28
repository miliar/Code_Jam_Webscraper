#define _HAS_CPP0X 0
#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:16777216")
#include <queue>
#include <cassert>
#include <sstream>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <iostream>
using namespace std;
typedef long long LL;
typedef vector<int> VI;
typedef pair<int, int> PII;
template<class T> T Abs(T x) { return x < 0 ? -x : x; }
#define FOR(i, n) for(int i = 0; i < (int)(n); ++i)


void Go(){
	int n, m;
	cin >> n >> m;
	vector<vector<int> > d(n, vector<int>(m));
	for (int i = 0; i < n; i++){
		for (int j = 0; j < m; j++){
			cin >> d[i][j];
		}
	}
	vector<vector<int> > dd(n, vector<int>(m, 100));
	for (int i = 0; i < n; i++)
	{
		int mr = d[i][0];
		for (int j = 1; j < m; j++){
			mr = max(mr, d[i][j]);
		}
		for (int j = 0; j < m; j++){
			dd[i][j] = min(dd[i][j], mr);
		}
	}
	for (int j = 0; j < m; j++)
	{
		int mc = d[0][j];
		for (int i = 1; i < n; i++){
			mc = max(mc, d[i][j]);
		}
		for (int i = 0; i < n; i++){
			dd[i][j] = min(dd[i][j], mc);
		}
	}
	bool ok = true;
	for (int i = 0; i < n; i++){
		for (int j = 0; j < m; j++){
			if (dd[i][j] != d[i][j]){
				ok = false;
			}
		}
	}
	if (ok){
		cout << "YES";
	}
	else{
		cout << "NO";
	}
}

int main(){
	const string task = "B";
	const string folder = "gcj/2013/qual";
	const int attempt = -1;
	const bool dbg = 0;


	if (dbg){
		freopen("inp.txt", "r", stdin);
	}
	else{
		stringstream ss;
		if (attempt < 0)
			ss << folder << '/' << task << "-large";
		else
			ss << folder << '/' << task << "-small-attempt" << attempt;
		freopen((ss.str() + ".in").c_str(), "r", stdin);
		freopen((ss.str() + ".out").c_str(), "w", stdout);
	}


	static char tt[128];
	gets(tt);
	int t;
	sscanf(tt, "%d", &t);
	FOR(i, t){
		printf("Case #%d: ", i + 1);
		Go();
		printf("\n");
	}
	return 0;
}