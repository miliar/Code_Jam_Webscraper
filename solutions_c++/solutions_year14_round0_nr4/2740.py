#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <string>
#include <queue>
#include <map>
using namespace std;
double s[10000], t[10000];
int n, T, war, d_war, v[10000];
int match[10000];
bool bi(int x){
	for(int i = 0; i < n; i++)
		if(s[x] > t[i] && !v[i]){
			v[i] = 1;
			if(match[i] == -1 || bi(match[i])){
				match[i] = x;
				return true;
			}
		}
	return false;
}
int main(){	
	//freopen("in", "r", stdin);
	//freopen("out", "w", stdout);
	cin >> T;
	for(int ct = 1; ct <= T; ct++){
		war = d_war = 0;
		cin >> n;
		for(int i = 0; i < n; i++)
			cin >> s[i];
		for(int j = 0; j < n; j++)
			cin >> t[j];
		sort(s, s+n);
		sort(t, t+n);
		memset(v, 0, sizeof(v));
		for(int i = 0; i < n; i++)
			match[i] = -1;
		for(int i = 0; i < n; i++)
			d_war += bi(i);
		memset(v, 0, sizeof(v));
		for(int i = 0; i < n; i++){
			match[i] = -1;
			double temp = s[i];
			s[i] = t[i];
			t[i] = temp;
		}
		for(int i = 0; i < n; i++)
			war += bi(i);
		printf("Case #%d: %d %d\n", ct, d_war, n-war);
	}
	return 0;
}
