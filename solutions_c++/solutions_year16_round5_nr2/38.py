#include<stdio.h>
#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
#include<memory.h>
#include<map>
#include<set>
#include<queue>
#include<list>
#include<sstream>
#define mp make_pair
#define pb push_back      
#define F first
#define S second
#define SS stringstream
#define sqr(x) ((x)*(x))
#define m0(x) memset(x,0,sizeof(x))
#define m1(x) memset(x,63,sizeof(x))
#define CC(x) cout << (x) << endl
#define pw(x) (1ll<<(x))
#define M 1000000007
#define N 1111
using namespace std;
typedef pair<int,int> pt;

vector<int> v[N];

string ch[N];

double C[222][222];
int n;

double rr() {
	long long t = 0;
	for (int i = 0; i < 3; i++) t = t * pw(14) + rand() % pw(14);
	return t / 1. / pw(14 * 3);
}

string merg(string &a, string &b) {
	if (a == "") return b;
	if (b == "") return a;

	int x = 0;
	int y = 0;
	string ret = "";
	while (x < a.size() && y < b.size()) {
		double tot = C[a.size() + b.size() - x - y][b.size() - y];
		double va = C[a.size() - 1 + b.size() - x - y][b.size() - y] / tot;
		double o = rr();
		if (o < va) {
			ret.pb(a[x]);
			x++;
		} else {
			ret.pb(b[y]);
			y++;
		}
	}
	if (x < a.size()) ret += a.substr(x);
	if (y < b.size()) ret += b.substr(y);

	return ret;
}

string getr(int x) {
	string ret = "";
	ret += ch[x];
	if (v[x].size() == 0) return ret;
	
	vector<string> f;

	string y = "";
	for (int i = 0; i < v[x].size(); i++) {
		f.pb(getr(v[x][i]));
	}
	while (f.size() > 1) {
		vector<pair<int, int> > hh;
		for (int i = 0; i < f.size(); i++) hh.pb(mp(f[i].size(), i));
		sort(hh.begin(), hh.end());
		int x = hh[0].S;
		int y = hh[1].S;

		f[x] = merg(f[x], f[y]);
		f[y] = f.back();
		f.pop_back();
	}
	return ret + f[0]; 
}

const int II = 5000;

int main(){
	freopen("1.in","r",stdin);	
	freopen("1.out","w",stdout);
	for (int i = 0; i <= 201; i++) for (int j = 0; j <= i; j++) if (i == j || j == 0) C[i][j] = 1;	else
		C[i][j] = C[i - 1][j] + C[i - 1][j - 1];

	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt++) {
		cin >> n;
		for (int i = 0; i <= n; i++) v[i].clear();
		for (int i = 1; i <= n; i++) {
			int x;
			cin >> x;
			v[x].pb(i);
		}
		string gg;
		cin >> gg;
		ch[0] = "";
		for (int i = 1; i <= n; i++) ch[i] = string() + gg[i - 1];
		int m;
		cin >> m;
		string te[m];
		for (int i = 0; i < m; i++) cin >> te[i];
		double ans[m];
		for (int i = 0; i < m; i++) ans[i] = 0;

		for (int it = 0; it < II; it++) {
			string b = getr(0);
//			cout << b << endl;
			for (int j = 0; j < m; j++) if (b.find(te[j]) < b.size()) ans[j]++;
		}
		for (int i = 0; i < m; i++) ans[i] /= II;


		cout << "Case #" << tt << ":";
		for (int i = 0; i < m; i++) printf(" %.5lf", ans[i]);
		cout << endl;

	}
	return 0;
}