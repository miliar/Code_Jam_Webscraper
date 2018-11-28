/*_______SHREY MANIK______*/
#include <iostream>
#include <string>
#include <climits>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <algorithm>
#include <utility>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cstring>
#include <iomanip>
#define MOD 1000000007
#define LL long long
#define SET(a) memset(a,-1,sizeof(a))
#define CLEAR(a) memset(a,0,sizeof(a))
#define mp(a,b) make_pair(a,b)
#define pb(a) push_back(a)
using namespace std;
template<class T>T gcd(T a,T b){return (b==0)?a:gcd(b,a%b);}
template<class T>T lcm(T a,T b){return (a*b)/gcd(a,b);}
int res[100005][5],dab[15][15],l,r,arr[100005];
int t,flag;
int ans;
char str[100005];
int k=0;
int main()
{

	freopen("source.txt","r",stdin);
    freopen("output.txt","w",stdout);
	scanf("%d",&t);while(t--){
	scanf("%d %d",&l,&r);
	scanf("%s",str);
	for(int i=0;i<r;i++)
	{
	for(int j=0;j<l;j++)
		{
	if(str[j]=='i')
			arr[i*l+j]=2;
			else if(str[j]=='j')
			arr[i*l+j]=3;
			else if(str[j]=='k')
			arr[i*l+j]=4;
			}
		}
		dab[1][1]=1;
 dab[1][2]=2; dab[1][3]=3;
              dab[1][4]=4;
		dab[2][1]=2;
           dab[2][2]=-1; dab[2][3]=4; dab[2][4]=-3;
		dab[3][1]=3;
         dab[3][2]=-4; dab[3][3]=-1;
         dab[3][4]=2;
		dab[4][1]=4;
            dab[4][2]=3;
      dab[4][3]=-2; dab[4][4]=-1;
		l=l*r;
		CLEAR(res);
		ans=arr[0];
		if(ans==2)
			res[0][2]=1;
		for(int i=1;i<l;i++)
		{
			if(ans>0)
				ans=dab[ans][arr[i]];
			else
				ans=-1*dab[abs(ans)][arr[i]];
			if(ans==2)
				res[i][2]=1;
		}
		ans=1;
		for(int i=0;i<l;i++)
		{
			if(res[i][2]==1)
			{
				ans=1;
				for(int j=i+1;j<l;j++)
				{
				if(ans>0)
					ans=dab[ans][arr[j]];
					else
					ans=-1*dab[-1*ans][arr[j]];
					if(ans==3)
					res[j][3]=1;

				}
			}
		}
		ans=1;
		flag=0;
		for(int i=0;i<l;i++)
		{
		if(res[i][3]==1)
			{				ans=1;
			for(int j=i+1;j<l;j++)
				{
				if(ans>0)
					ans=dab[ans][arr[j]];
				else
						ans=-1*dab[-1*ans][arr[j]];
				}
				if(ans==4)
				{
					flag=1;
					break;
				}
			}

		}
++k;
		if(flag==1)
			printf("Case #%d: YES\n",k);
		else
			printf("Case #%d: NO\n",k);
	}
	return 0;
}
