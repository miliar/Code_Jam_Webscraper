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
using namespace std;

typedef long long ll;
const int N = 1e6 + 5;
vector<bool>g;
bool move(vector<bool>v){
	g.clear();
	int z = 0;
	while (v.size() && !v.back())
		v.pop_back();
	for (int i = 0; i < v.size(); ++i){
		z += v[i];
		g.push_back(!v[i]);
	}
	if (!z){
		g = v;
		return 1;
	}
	if (z == v.size())
		return 0;
	if (!v[0]){
		v[0] = !v[0];
		g = v;
		return 0;
	}
	reverse(v.begin(), v.end());
	g.clear();
	for (int i = 0; i < v.size(); ++i)
		g.push_back(!v[i]);
	return 0;
}
int main(){
	freopen("BinL.txt", "r", stdin);
	freopen("BoutL.txt", "w", stdout);
	int t;
	cin >> t;
	for (int k = 1; k <= t; ++k){
		string x;
		cin >> x;
		int n = x.size();
		vector<bool>v;
		for (int i = 0; i < n; ++i){
			x[i] = (x[i] != '+');
			if (!i || v.back() != x[i])
				v.push_back(x[i]);
		}
		int res = 0;
		if (v.size() == 1)
			res = v[0];
		else{
			while (!move(v)){
				++res;
				v = g;
			}
		}
		printf("Case #%d: %d\n", k, res);
	}
}