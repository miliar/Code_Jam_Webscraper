#include<vector>
#include<cstring>
#include<algorithm>
#include<stdio.h>
#include<climits>
#include<set>
#include<cmath>
#include<bitset>
#include<map>
#include<iostream>
#include<queue>
#define test(t) while(t--)
#define s(n) scanf("%d",&n)
#define sl(n) scanf("%llu",&n)
 
#define p(n) printf("%llu\n",n)
#define rep(i,a,n) for(i=a;i<=n;i++)
#define vi vector<int>
#define vii vector< vector<int> >
#define vpii vector< pair<int,int> >
#define mii map<int,int>
#define pb push_back
#define inf 1000000000LL
#define mp make_pair
#define MOD 1000000009LL
#define ll long long
#define gc getchar_unlocked
using namespace std;
int main()
{
	
int t,i;
double c,f,x;
double ans,tmp,tmp1,finalans;
double div;
s(t);
for(i=1;i<=t;++i)
{
	ans=0.0;
	div=2.0;
	scanf("%lf%lf%lf",&c,&f,&x);
	tmp=x;
	finalans=(double)((double)tmp/(double)div);
	while((tmp-c)>0.0)
	{
		tmp=tmp-c;
		ans=ans+(double)((double)c/(double)div);
		div=div+f;
		tmp1=ans+(double)((double)x/(double)div);
		if(finalans-tmp1>0.0)
		finalans=tmp1;
	}

	printf("Case #%d: %0.7lf\n",i,finalans);
}
return 0;
}
