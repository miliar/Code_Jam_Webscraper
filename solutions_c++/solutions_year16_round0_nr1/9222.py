#include <bits/stdc++.h>

#define pb push_back
#define mp make_pair
#define f first
#define s second
#define all(x) x.begin(),x.end()
#define rall(x) x.rbegin(),x.rend()
#define pi acos(-1.0)
#define EPS 1e-9
#define mem(n,x) memset(n,x,sizeof(n))
typedef long long ll;

using namespace std;

bool vis[10];
int cnt;

bool check(int x){
	while(x>0){
		if(!vis[x%10])
			vis[x%10]=1, ++cnt;
		x/=10;
	}
	return (cnt==10);
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int T;scanf("%d",&T);

	for(int cs=1;cs<=T;++cs){
		int n;scanf("%d",&n);

		printf("Case #%d: ",cs);

		if(!n){printf("INSOMNIA\n");continue;}


		mem(vis,0);cnt=0;
		for(int i=1;;++i){
			if(check(n*i)){printf("%d\n",n*i);break;}
		}
	}
	return 0;
}
