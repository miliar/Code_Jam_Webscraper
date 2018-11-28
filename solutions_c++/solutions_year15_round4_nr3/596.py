										/* in the name of Allah */
#include <algorithm>
#include <iostream>
#include <memory.h>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <cmath>
#include <list>
#include <map>
#include <set>

using namespace std;

#define uint unsigned int
#define int64 long long
#define P pair<int, int>
#define Pss pair<string, string>
#define PLL pair<int64, int64>
#define Inf 1000000
#define Mod 1000000007LL

int n;
vector <int> w[30];
set <int> st[2], dm[2];
set <int> shr;

int hsh(string str){
	int B = 41;
	int res = 1;
	for(int i = 0; i < str.length(); i++)
		res = res * B + (str[i] - 'a');
	return res;
}

void inp(int idx, bool check){
	string str;
	getline(cin, str);
	istringstream sin(str);
	w[idx].clear();
	string tmp;
	while(sin >> tmp){
		int x = hsh(tmp);
		if(!check || !shr.count(x))
			w[idx].push_back(hsh(tmp));
	}
}

int main(){
	long long t0 = clock();
	freopen("C-Bilingual.in", "r", stdin);
	freopen("C-Bilingual.out", "w", stdout);
	int T, test = 0;
	for(cin >> T; T--; ){
		cin >> n;
		cin.ignore();
		cerr << T << ' ' << n << endl;
		for(int i = 0; i < 2; i++)
			inp(i, false);
		st[0].clear();
		st[1].clear();
		for(int k = 0; k < 2; k++)
			for(int i = 0; i < w[k].size(); i++)
				st[k].insert(w[k][i]);
		shr.clear();
		for(set <int>::iterator it = st[0].begin(); it != st[0].end(); it++)
			if(st[1].count(*it))
				shr.insert(*it);
		for(set <int>::iterator it = shr.begin(); it != shr.end(); it++){
			int val = *it;
			st[0].erase(val);
			st[1].erase(val);
		}

		for(int i = 2; i < n; i++)
			inp(i, true);
		int mn = 1000000;
		for(int mask = 2; mask < (1 << n); mask += 4){
			dm[0].clear();
			dm[1].clear();
			for(int i = 2; i < n; i++){
				for(int j = 0; j < w[i].size(); j++){
					int p = ((mask >> i) & 1);
					if(!st[p].count(w[i][j]))
						dm[p].insert(w[i][j]);
				}
			}

			int cnt = 0;
			for(set <int>::iterator it = dm[0].begin(); it != dm[0].end(); it++)
				if(st[1].count(*it) || dm[1].count(*it))
					cnt++;
			for(set <int>::iterator it = dm[1].begin(); it != dm[1].end(); it++)
				if(st[0].count(*it))
					cnt++;
			mn = min(mn, cnt);
		}
		cout << "Case #" << ++test << ": " << shr.size() + mn << endl;
		cerr << (clock() - t0) / CLOCKS_PER_SEC << endl;
		t0 = clock();
	}
	return 0;
}
