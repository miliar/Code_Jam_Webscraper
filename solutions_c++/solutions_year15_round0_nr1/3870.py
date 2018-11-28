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
const double eps = 1e-8;
const ll mod = 1e9 + 7;

int n;
char ts[1005];

int main()
{
	int T,R;
	R=0;
	scanf("%d",&T);
	while(T--)
	{
		R++;
		scanf("%d",&n);
		scanf("%s",ts);
		int i,j;
		int sum;
		int ans;
		sum=ans=0;
		sum=ts[0]-'0';
		for(i=1;i<=n;i++)
		{
			if(ts[i]-'0'==0)
				continue;
			if(sum>=i)
				sum+=ts[i]-'0';
			else
			{
				ans+=i-sum;
				sum=i+ts[i]-'0';
			}
		}
		printf("Case #%d: %d\n",R,ans);
	}
	return 0;
}