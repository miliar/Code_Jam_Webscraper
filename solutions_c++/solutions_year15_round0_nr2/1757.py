#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
using namespace std;
int max(int a, int b){
	if(a>b)return a;
	return b;
}
int min(int a, int b){
	if(a>b)return b;
	return a;
}
int main(){
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int casenum = 1;casenum<=t;casenum++){
		int ans = 0;
		int p[1100];
		int n;
		scanf("%d", &n);
		int m = -1;
		for(int i = 0;i<n;++i){
			scanf("%d", &p[i]);
			m = max(m, p[i]);
			ans += p[i]-1;
		}
		ans+=1;
		ans = min(m, ans);
		for(int i = 2;i<m;i++){
			int tmp = 0;
			for(int j = 0;j<n;j++){
				tmp+=p[j]/i;
				if(p[j]%i==0)tmp--;
			}
			tmp+=i;
			ans = min(tmp, ans);
		}
		printf("Case #%d: %d\n", casenum, ans);
	}
	return 0;
}