#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <stdio.h>
#include <vector>
#include <string>
#include <memory.h>
#include<map>
using namespace std;
typedef long long ll;
string x[16], y[16];
int X[16], Y[16];
map<string, int>mp;
int id;
int find(string x){
	if (mp.find(x) == mp.end())
		return mp[x] = id++;
	return mp[x];
}
int main(){
	freopen("src.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for (int k = 1; k <= t; ++k){
		id = 0; int n;
		cin >> n;
		mp.clear();
		for (int i = 0; i < n; ++i){
			cin >> x[i] >> y[i];
			X[i] = find(x[i]), Y[i] = find(y[i]);
		}
		int b = 0;
		vector<pair<int, int> >msk;
		for (int i = 0; i < (1 << n) - 1; ++i){
			int I = i, c = 0;
			while (I){ c += I & 1; I /= 2; }
			msk.push_back(make_pair(c, i));
		}
		sort(msk.begin(), msk.end());
		for (int ii = 0; ii < msk.size(); ++ii){
			int i = msk[ii].second;
			vector<pair<int, int> > g;
			bool first[35] = { 0 }, second[35] = { 0 };
			int S = 0, SS = 0;
			for (int j = 0; j < n; ++j){
				int A = X[j], B = Y[j];
				if ((i >> j) & 1){
					first[A] = second[B] = 1;
					SS++;
				}
				else g.push_back(make_pair(A, B));
			}
			int c = 0;
			int I = i;
			while (I){ c += I & 1; I /= 2; }
			
			for (int i = 0; i < g.size(); ++i){
				if (first[g[i].first] && second[g[i].second]){
					++S;
				}
				else break;
			}
			if (SS + S == n){
				b = g.size();
				break;
			}
		}
		printf("Case #%d: %d\n", k, b);
	}
}

// "THREE", , "SEVEN", , "NINE"