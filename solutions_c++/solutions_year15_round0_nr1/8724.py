#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<queue>
#include<stack>
#include<vector>
#include<set>
#include<map>


#define L(x) (x<<1)
#define R(x) (x<<1|1)
#define MID(x,y) ((x+y)>>1)

#define eps 1e-8
typedef long long ll;

#define fre(i,a,b)  for(i = a; i <b; i++)
#define free(i,b,a) for(i = b; i >= a;i--)
#define mem(t, v)   memset ((t) , v, sizeof(t))
#define ssf(n)      scanf("%s", n)
#define sf(n)       scanf("%d", &n)
#define sff(a,b)    scanf("%d %d", &a, &b)
#define sfff(a,b,c) scanf("%d %d %d", &a, &b, &c)
#define pf          printf
#define bug         pf("Hi\n")

using namespace std;

#define INF 0x3f3f3f3f
#define N 10005

int a[N];

int main()
{
   	int i,j,t,ca=0;
   	int n;
   	freopen("C:/Users/asus1/Downloads/A-large.IN","r",stdin);
   	freopen("C:/Users/asus1/Downloads/out.txt","w",stdout);

   	sf(t);
   	while(t--)
	{
		sf(n);
		for(i=0;i<=n;i++)
			scanf("%1d",&a[i]);

	    int temp=a[0];
	    int ans=0;

	    for(i=1;i<=n;i++)
		{
			if(temp<i)
				{
					ans+=i-temp;
				    temp+=i-temp;
				}

		      temp+=a[i];
		}
		pf("Case #%d: ",++ca);
		pf("%d\n",ans);
	}
   return 0;
}
