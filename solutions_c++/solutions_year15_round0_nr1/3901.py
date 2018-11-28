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

char s[1005];
int main()
{
	int i,j,k,n,t,res=0;
	scanf("%d",&t);
	while(t--){
		res++;
	scanf("%d%s",&n,s);
	int ans=0;
	int sum=s[0]-'0';
	for(i=1;i<=n;i++)
	{
		if(sum>=i)
			sum+=s[i]-'0';
		else
		{
			ans+=i-sum;
			sum=i;
			sum+=s[i]-'0';
		}
	}
	printf("Case #%d: %d\n",res,ans);
	}
}