#define _CRT_SECURE_NO_WARNINGS
#pragma comment (linker, "/STACK:16777216")
#include <algorithm>
#include <numeric>
#include <string>
#include <string.h>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <iostream>
#include <fstream>
#include <cmath>
#include <math.h>
#include <iomanip>
#include <stdlib.h>
#include <time.h>
#include <sstream>
#include <stdio.h>
#include <stack>
#include <time.h>

using namespace std;

#define FOR(i,n) for (int i=0; i<n; ++i)
#define FORE(i,n) for (int i=0; i<=n; ++i)
#define REP(i,a,b) for (int i=a; i<b; ++i)
#define REPE(i,a,b) for (int i=a; i<=b; ++i)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define mp make_pair
#define pb push_back
#define INF (1e9)

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef long long int LL;
typedef vector<LL> VI;
typedef vector<bool> VB; 
typedef vector<VI> VVI;
const long double pi = 3.14159265358979323846;
const int inf = (int)1e9;

const LL base=inf;

bool pred (const string& i, const string& j)
{
    return i.size()<j.size();
}

int n;
vector<string> s(105);
string a;
int res = inf;

int go(string &z1) {
	int res = 0;
	FOR(i,n) {
		if (s[i] == z1) {
			continue;
		}
		string z2 = s[i];
		int x = 0;
		int y = 0;		
		while(x < z1.size()) {
			if (z1[x] != z2[y]) {
				return -1;
			}
			int x1 = x;
			while(x < z1.size() && z1[x] == z1[x1]) {
				++x;
			}
			int y1 = y;
			while(y < z2.size() && z2[y] == z2[y1]) {
				++y;
			}
			int c1 = x - x1;
			int c2 = y - y1;
			
			res += abs(c1 - c2);
		}
		if (y < z2.size()) {
			return -1;
		}
	}
	return res;
}

int solve() {	
	FOR(i,n) {
		string z = s[i];
		int now = go(z);
		if (now == -1) {
			return -1;
		}
		res = min(now,res);
	}
	return res;
}

bool checkFegla() {
	vector<string> z(n, "");
	FOR(i,n) {
		FOR(j,s[i].size()) {
			if (!j || s[i][j] != s[i][j - 1]) {
				z[i] += s[i][j];
			}
		}
	}
	a = z[0];
	FOR(i,n) {
		if (z[i] != z[0]) {
			return true;
		}
	}
	return false;
}

int main(){
#ifdef _DEBUG
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#else
   // freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
#endif  
	int t;
	cin >> t;
	FOR(tt,t) {
		cout << "Case #" << tt + 1 << ": ";
		cin >> n;	
		FOR(i,n) {
			cin >> s[i];
		}
		if (checkFegla()) {
			cout << "Fegla Won\n";
			continue;
		}
		res = inf;
		res = min(solve(), go(a));
		cout << res << "\n";
	}
    return 0;
}