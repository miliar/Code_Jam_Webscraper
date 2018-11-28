#include<bits/stdc++.h>
using namespace std;
#define MOD 1000000007
#define lim 1000
#define f first
#define s second
#define lli long long int
#define mp(x,y) make_pair(x,y)
#define pii pair<int,int>
#define vii vector<int>
#define vvi vector<pii>
#define pb push_back
#define sc(x) scanf("%d",&x)
#define ms(a,y) memset(a,y,sizeof(a))
#define all(x) x.begin(),x.end()
#define pi 3.14159
int main()
{
	freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t,i=1;
	sc(t);
	while(t--)
	{
		lli n;
		scanf("%lld",&n);
		printf("Case #%d: ",i++);
		if(!n)
		printf("INSOMNIA\n");
		else
		{
			int a[10]={0};
			lli x,z=1;
			while(true)
			{
				bool flag=true;
				x=z*n;
				++z;
				while(x)
				{
					++a[x%10];
					x/=10;
				}
				for(int j=0;j<10;++j)
				if(!a[j])
				{
					flag=false;break;
				}
				if(flag) break;
			}
			printf("%lld\n",(z-1)*n);
		}
	}
 	return 0;
}

