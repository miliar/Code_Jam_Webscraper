//#pragma comment(linker,"/STACK:16777216") /*16Mb*/
//#pragma comment(linker,"/STACK:33554432") /*32Mb*/
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <stack>
#include <cmath>
#include <list>
#include <iomanip>
#include <set>
#include <map>
using namespace std;

typedef  long long LL;
typedef  unsigned long long ULL;
typedef  long double LD;
typedef  pair<int,int> PII;

#define FOR(i,a,b) for(int (i)=(a);i<(b);++(i))
#define RFOR(i,a,b) for(int (i)=(a)-1;(i)>=(b);--(i)) 
#define MP make_pair
#define MOD 1000000007
#define INF 1000000000
#define PB push_back

int t,n;
LL a,b[1000001];
int main()
{
	//ios_base::sync_with_stdio(0);
	freopen("A-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	FOR(ttt,0,t)
	{
		scanf("%d%d",&a,&n);
		FOR(i,0,n)
			scanf("%d",&b[i]);
		sort(b,b+n);
		int ans=0;
		FOR(i,0,n)
		{
			if(a<=b[i])
			{
				if(a==1){ans=n-i;break;}
				int k=0;
				while(a<=b[i])
				{
					++k;
					a+=a-1;
				}
				if(k<n-i)
					ans+=k;
				else
				{
					ans+=n-i;
					break;
				}
			}
			a+=b[i];
		}
			printf("Case #%d: %d\n",ttt+1,ans);
	}
	return 0;
}