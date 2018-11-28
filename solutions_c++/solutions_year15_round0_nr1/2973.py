/******************************************************
 * File Name:   a.cpp
 * Author:      kojimai
 * Create Time: Fri 10 Apr 2015 06:12:18 PM CST
******************************************************/

#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<iostream>
using namespace std;
char s[1005];
int main() {
	int T,n;
	cin >> T;
	freopen("out.out","w",stdout);
	for(int Cas = 1;Cas <= T;Cas++) {
		int ans = 0,now = 0;
		cin >> n >> s;
		for(int i = 0;i <= n;i++) {
			if(now < i) {
				ans += i - now;
				now = i;
			}
			now += s[i] - '0';
		}
		printf("Case #%d: %d\n",Cas,ans);
	}
	return 0;
}
