#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<cmath>
#include<queue>
#include<map>
#define fo(i,a,b) for(int i=a;i<=b;i++)
#define fd(i,a,b) for(int i=a;i>=b;i--)
#define ld long double
using namespace std;

ld gaili[205];

int TEST,number,pq;

int choo[205];

ld pri;

ld dp[205][205];

ld gpp[205];

void just_dp(){
	fo(i,1,choo[0]) gpp[i]=gaili[choo[i]];
	memset(dp,0,sizeof(dp));
	dp[0][0]=1.0;
	fo(i,1,pq) {fo(j,1,pq) {dp[i][j]=dp[i-1][j]*(1-gpp[i])+dp[i-1][j-1]*gpp[i];}
		dp[i][0]=dp[i-1][0]*(1-gpp[i]);
	}
	pri=max(pri,dp[pq][pq / 2]);
}

void digui(int pla,int totcho) {
	if (totcho>pq) return;
	if (pla==number+1) {
		if (totcho!=pq) return;
			just_dp();
		return;
	}
	digui(pla+1,totcho);
	choo[++choo[0]]=pla;
	digui(pla+1,totcho+1);
	--choo[0];
}

int main(){
	freopen("2.in", "r", stdin);
	freopen("2.out", "w", stdout);
	cin>>TEST;
	fo(num_cho,1,TEST) {
		printf("Case #%d: ",num_cho);
		cin>>number>>pq;
			fo(i,1,number) cin>>gaili[i];
		pri=0;
		digui(1,0);
		double ans=pri;
		printf("%.10lf",ans);
		puts("");
	}
	return 0;
}
