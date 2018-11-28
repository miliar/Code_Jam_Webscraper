#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pi pair<int,int>
#define F first
#define S second
#define MAXN 100005
#define MOD 1000000007

int a[MAXN];
int main()
{
	ll n,m,p;
	int t,tt,i,j;
	cin >>tt;
	for(t=1;t<=tt;t++){
		cin >> n >> m;
		printf("Case #%d: ",t);
		p=(1ll<<(n-2));
		if(m>p){
			puts("IMPOSSIBLE");
			continue;
		}
		puts("POSSIBLE");
		printf("0");
		for(i=2;i<=n;i++){
			p/=2;
			if(m>=p && m>0){
				printf("1");
				m-=p;
			}
			else
				printf("0");
		}
		puts("");
		for(i=2;i<=n;i++){
			for(j=1;j<=i;j++)
				printf("0");
			for(;j<=n;j++)
				printf("1");
			puts("");
		}
	}
	return 0;
}