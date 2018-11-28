#include<stdio.h>
#include<algorithm>
#include<iostream>
using namespace std;
#define N  1010
#define ll long long
double const PI=3.1415926;
double const ESP=1e-7;
char s1[N],s2[N];
int dp[N][N];

ll r,t,cur;
double v,need;
int main()
{
	int re,Case=1;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	scanf("%d",&re);
	while(re--){
		scanf("%lld%lld",&r,&t);
        v=t*PI;
		cur=r+1;
        int cnt=0;
		for(;;cur+=2){
			need=PI*( cur*cur-(cur-1)*(cur-1) );
			if(need<v || abs(need-v)<ESP){ v-=need; cnt++; }
			else break;
		}
		printf("Case #%d: %d\n",Case++,cnt);
	}
}