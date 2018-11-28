#define _CRT_SECURE_NO_WARNINGS
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<cmath>
#include<string>
#include<vector>
#include<cctype>
#include<bitset>
#include<sstream>
#include<stdio.h>
#include<cstring>
#include<fstream>
#include<iostream>
#include<algorithm>
#include<limits.h>
#define mp make_pair
using namespace std;
int dx[] = { 0, 0, 1, -1 };
int dy[] = { 1, -1, 0, 0 };
int main(){
#ifndef ONLINE_JUDGE
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#endif
	int t,n;
	cin >> t;
	for (int i = 1; i <= t; ++i){
		cin >> n;
		vector<int>v(n);
		for (int j = 0; j < n; ++j)
			cin >> v[j];
		int s1 = 0, s2 = 0;
		int mx = 0;
		for (int j = 0; j < v.size()-1; ++j){
			mx = max(mx,v[j] - v[j + 1]);
			if (v[j + 1] < v[j])
				s1 += abs(v[j + 1] - v[j]);
		}
		for (int j = 0; j < n - 1; ++j){
			if (v[j] <= mx)
				s2 += v[j];
			else
				s2 += mx;
		}
		printf("Case #%d: %d %d\n", i, s1, s2);
	}
	return 0;
}
