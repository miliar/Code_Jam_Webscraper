/******************************************************
 * File Name:   b.cpp
 * Author:      kojimai
 * Create Time: Fri 10 Apr 2015 06:31:08 PM CST
******************************************************/

#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<iostream>
using namespace std;
#define FFF 1005
int a[FFF];
bool cmp(int x,int y) {
	return x > y;
}

int main() {
	int T,n;
	//freopen("out.out","w",stdout);
	scanf("%d",&T);
	for(int Cas = 1;Cas <= T;Cas++) {
		scanf("%d",&n);
		for(int i = 0;i < n;i++) {
			scanf("%d",&a[i]);
		}
		sort(a,a+n,cmp);
		int ans = a[0];
		for(int i = a[0] - 1;i >= 2;i--) {
			int now = 0;
			for(int j = 0;a[j] > i && j < n && now < ans;j++) {
				now += (a[j]  - 1) / i;
			}
			now += i;
			//cout<<"i = "<<i<<" now = "<<now<<endl;
			if(now < ans)
				ans = now;
		}
		printf("Case #%d: %d\n",Cas,ans);
	}
	return 0;
}
