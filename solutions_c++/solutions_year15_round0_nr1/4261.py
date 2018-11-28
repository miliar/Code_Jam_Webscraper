#include<cstdio>
#include<cstring>
#include<algorithm>
#define fou(i,j,k) for (int i=j;i<=k;i++)
#define fod(i,j,k) for (int i=j;i>=k;i--)
using namespace std;

typedef long long LL;

const int maxn=1010;

char str[maxn];

void solve()
{
	int n,sum,ans,x;
	scanf("%d%s",&n,str);
	sum=0;ans=0;
	fou(i,0,n){
		x=str[i]-'0';
		if (sum<i){
			ans+=i-sum;
			sum+=i-sum;
		}
		sum+=x;
	}
	printf("%d\n",ans);
}

int main()
{
	int T;
	scanf("%d",&T);
	fou(i,1,T){
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}
