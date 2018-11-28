// GCJ Oversized Pancake Flipper.cpp : 定义控制台应用程序的入口点。
//

//#include "stdafx.h"
#include<iostream>
#include<cstring>
#include<cmath>
#include<cstdio>
#include<algorithm>
using namespace std;
int t, k;
const int MAXN = 2e3 + 10;;
char s[MAXN];
int vv[MAXN];//
int main(){
	//freopen("in.in", "r", stdin);
	//freopen("out.out", "w", stdout);
	cin >> t;
	int kase = 0;
	while (t--){
		++kase;
		cin >> s >> k;
		int len = strlen(s);
		int ans = 0;
		memset(vv, 0, sizeof vv);
		int ti = 0;
		bool ff = true;
		for (int i = 0; i < len; ++i){
			ti += vv[i];
			if (s[i] == '-'&&ti % 2){
				continue;
			}
			else if (s[i] == '+'&&ti % 2 == 0){
				continue;
			}
			if (i + k > len){
				ff = false;
				break;
			}
			++ti;
			++ans;
			++vv[i + k];
		}
		printf("Case #%d: ", kase);
		if (ff)cout << ans << endl;
		else cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}

