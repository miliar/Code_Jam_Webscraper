#include<iostream>
#include<cstring>
#include<algorithm>
#include<cstdlib>
#include<vector>
#include<cmath>
#include<stdlib.h>
#include<iomanip>
#include<list>
#include<deque>
#include<map>
#include <stdio.h>
#include <queue>
#include <stack>
#define maxn 10000+5
#define ull unsigned long long
#define ll long long
#define reP(i,n) for(i=1;i<=n;i++)
#define rep(i,n) for(i=0;i<n;i++)
#define cle(a) memset(a,0,sizeof(a))
#define mod 90001
#define PI 3.141592657
#define INF 1<<30
const ull inf = 1LL << 61;
const double eps=1e-5;

using namespace std;

bool cmp(int a,int b)
{
    return a>b;
}
char s[1100];
int a[1100];
int main()
{
    #ifndef ONLINE_JUDGE
    freopen("A-large.in","r",stdin);
    #endif
    freopen("out.txt","w",stdout);
    int n;
    int t;
    cin>>t;
	for(int j=1;j<=t;j++){
		a[0]=0;
		scanf("%d %s",&n,s);
		for(int i=0;i<=n;i++){
			a[i]=(int)(s[i]-'0');
		}
		ll sum=a[0],ans=0;
		for(int i=1;i<=n;i++){
			if(sum<i&&a[i]!=0)ans+=i-sum,sum+=i-sum;
			sum+=a[i];
		}
		printf("Case #%d: %I64d\n",j,ans);
    }
    return 0;
}
