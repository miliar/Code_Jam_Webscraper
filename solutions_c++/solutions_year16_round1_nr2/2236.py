/******************************************************
 * File Name:   b.cpp
 * Author:      kojimai
 * Create Time: Fri 15 Apr 2016 06:46:28 PM PDT
******************************************************/

#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<iostream>
using namespace std;
#define FFF 55
int a[FFF][FFF];
int cnt[2505];
int main() {
	int T;
	freopen("out.out","w",stdout);
	cin >> T;
	for(int Cas = 1;Cas <= T;Cas++) {
		int n;
		printf("Case #%d:",Cas);
		memset(cnt,0,sizeof(cnt));
		cin >> n;
		for(int i = 0;i < 2*n-1;i++) {
			for(int j = 0;j < n;j++) {
				cin >> a[i][j];
				cnt[a[i][j]]++;
			}
		}
	
		for(int i = 1;i <= 2500;i++) {
			if(cnt[i] % 2 == 1) {
					printf(" %d",i);
			}
		}
		cout << endl;
	}
	return 0;
}