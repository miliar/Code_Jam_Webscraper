#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <map>
#include <set>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <utility>
#include <cstring>
#include <list>
#include <stack>
using namespace std;

#define ft first
#define sd second

typedef long long LL;
typedef unsigned int UI;

const int MAXN = 511111;
const int MOD = 1e9 + 7;
const double eps = 1e-6;
const LL MAXL = (LL)(0x7fffffffffffffff);
const int MAXI = 0x7fffffff;

int res[5][5] = {
	{ 0, 0, 0, 0, 0 },
	{ 0, 1, 2, 3, 4 },
	{ 0, 2, 1, 4, 3 },
	{ 0, 3, 4, 1, 2 },
	{ 0, 4, 3, 2, 1 }
};

int sign[5][5] = {
	{ 0, 0, 0, 0, 0 },
	{ 0, 0, 0, 0, 0 },
	{ 0, 0, 1, 0, 1 },
	{ 0, 0, 1, 1, 0 },
	{ 0, 0, 0, 1, 1 }
};

int main(){

#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	
	int T;
	cin >> T;
	for(int cases = 1; cases <= T; cases++){
		int L, X;
		cin >> L >> X;
		string t;
		cin >> t;
		int len = L * X;
		vector<int> num(len);
		for(int i = 0; i < len; i++){
			char a = t[i % L];
			if(a == 'i') num[i] = 2;
			else if(a == 'j') num[i] = 3;
			else num[i] = 4;
		}
		vector<pair<int, int> > r(len);
		r[0] = make_pair(0, num[0]);
		for(int i = 1; i < len; i++){
			int s = r[i - 1].ft;
			r[i] = make_pair(sign[r[i - 1].sd][num[i]], res[r[i - 1].sd][num[i]]);
			r[i].ft ^= s;
		}/*
		if(cases == 2){
			for(int i = 0; i < len; i++){
				cout << r[i].ft << " " << r[i].sd << endl;
			}
		}*/
		bool yes = false;
		if(r[len - 1].ft && r[len - 1].sd == 1){
			int id = -1;
			for(int i = 0; i < len && !yes; i++){
				if(r[i].ft) continue;
				if(r[i].sd == 2){
					id = i;
				}
				else if(r[i].sd == 4){
					if(id != -1) yes = true;
				}
			}
		}
		printf("Case #%d: ", cases);
		cout << (yes ? "YES\n" : "NO\n");
	}
}
