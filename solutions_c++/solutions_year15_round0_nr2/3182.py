#include <cstdio>
#include <cstring>
#include <iostream>
#include <cmath>
#include <ctime>
#define ll long long
#define maxn 370000//状态数最多9的阶乘 
#define MOD 10000007//哈希表的mod值 
using namespace std;
int a[1020];
int T,size;


int n,ans;

int main()
{
//	freopen("B.in","r",stdin);
//	freopen("B.out","w",stdout);
	
	scanf("%d",&T);
	for(int ii=1;ii<=T;++ii)
	{
		size=0;
		scanf("%d",&n);
		for(int i=1;i<=n;++i)
		{
			scanf("%d",&a[i]);
		}
		ans = 1000;
		for(int i=1;i<=1000;++i)
		{
			int aug =0;
			for(int j=1;j<=n;++j)aug+=(a[j]-1)/i;
			ans=min(ans,aug+i);
		}
		printf("Case #%d: %d\n",ii,ans);
	}
    
    return 0;
    
}
