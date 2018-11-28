#include<map>
#include<string>
#include<cstring>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<queue>
#include<vector>
#include<iostream>
#include<algorithm>
#include<bitset>
#include<climits>
#include<list>
#include<iomanip>
#include<stack>
#include<set>
using namespace std;
typedef long long ll;
bool vis[10];
int main()
{
//	freopen("A-large.in","r",stdin);
//	freopen("A-large.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int cs=1;cs<=T;cs++)
	{
		memset(vis,0,sizeof(vis));
		int n;
		scanf("%d",&n);
		if(n==0)
		{
			printf("Case #%d: INSOMNIA\n",cs);
			continue;
		}
		int sum=0,i;
		for(i=1;;i++)
		{
			ll t=ll(i)*n;
			while(t)
			{
				if(!vis[t%10])
					sum++;
				if(sum==10)
					break;
				vis[t%10]=1;
				t/=10;
			}
			if(sum==10)
				break;
		}
		printf("Case #%d: ",cs);
		cout<<ll(i)*n<<endl;
	}
}
