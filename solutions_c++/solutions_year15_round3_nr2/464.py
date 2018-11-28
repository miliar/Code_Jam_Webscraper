#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<utility>
#include<queue>
#include<set>
#include<map>
#include<math.h>
#include<string>
#include<bitset>
#include <time.h>
using namespace std;
//#pragma warning(disable:4996)
#pragma comment(linker, "/STACK:102400000,102400000")
#define ll long long
#define mp make_pair 
#define pb push_back
#define pii pair<int,int>
#define mem(a,b) memset(a,b,sizeof(a))
#define maxn 110
#define inf 0x3f3f3f3f
const int dir[4][2]={0,1,0,-1,1,0,-1,0};
const double eps = 1e-9;
const ll mod = 1e9 + 7;

char ts1[10];
char ts2[10];
int n,m,ci;
double la[26];
int have[26];
int cnt;

int sum;
int temp[10];
double zuida;
double ans;

void check(double gailv)
{
	sum=0;
	int i,j;
	for(i=1;i+m-1<=ci;i++)
	{
		int flag=1;
		for(j=0;j<m;j++)
			if((ts2[j]-'A')!=temp[i+j])
			{
				flag=0;
				break;
			}
		if(flag==1)
			sum++;
	}
	if(sum>zuida)
		zuida=(double)sum;
	ans+=(double)sum*gailv;
}

void dfs(int ceng,double gailv)
{
	if(ceng==ci+1)
	{
		check(gailv);
		return ;
	}
	for(int i=0;i<cnt;i++)
	{
		temp[ceng]=have[i];
		dfs(ceng+1,gailv*la[have[i]]);
	}
}

int main()
{
	int T,R=0;
	scanf("%d",&T);
	while(T--)
	{
		R++;
		scanf("%d%d%d",&n,&m,&ci);
		scanf("%s",ts1);
		scanf("%s",ts2);
		int i,j;
		for(i=0;i<26;i++)
			la[i]=0.0;
		for(i=0;i<n;i++)
			la[ts1[i]-'A']+=1.0/(double)n;
		cnt=0;
		for(i=0;i<26;i++)
		{
			if(la[i]>0.0)
				have[cnt++]=i;
		}
		sum=0;
		ans=0;
		zuida=0.0;
		dfs(1,1.0);
		printf("Case #%d: %.7lf\n",R,zuida-ans);
	}
	return 0;
}