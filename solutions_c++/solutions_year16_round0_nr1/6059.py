#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string.h>
#include <bitset>
#include <queue>
#include <map>
#include <string>
#include <stack>
#include <utility>
#include <queue>
#include <cmath>
#define mp make_pair
#define pii pair<int,int> 
#define ff first
#define ss second
#define ll long long 
#define ull unsigned long long
#define vi vector<int>
#define vii vector<pii>
#define vvi vector <vi>
#define rep(x,a,b,c) for(int x=a;x<=b;x+=c)
#define repp(x,a,b) rep(x,a,b,1)
#define rev(x,a,b,c) for(int x=a;x>=b;x-=c)
#define revv(x,a,b) rev(x,a,b,1)
#define OO (int)2e9
#define INF (ll)9e18
 
using namespace std;

int tc,n,maxs,temp,finish;
bool cek[20];

int main()
{
	scanf("%d",&tc);
	repp(t,1,tc)
	{
		scanf("%d",&n);
		if(n==0)printf("Case #%d: INSOMNIA\n",t);
		else
		{
			memset(cek,0,sizeof(cek));
			finish=false;
			repp(x,1,100)
			{
				temp=n*x;
				while(temp>0)
				{
					cek[temp%10]=1;
					temp/=10;
				}
				repp(y,0,9)
				{
					if(cek[y]==0)
					{
						break;
					}
					if(y==9)
					{
						printf("Case #%d: %d\n",t,n*x);
						finish=true;
						break;
					}
				}
				if(finish)
				{
					break;
				}
			}
		}
	}
	return 0;
}
