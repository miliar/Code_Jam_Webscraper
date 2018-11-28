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

char tmp[200];
int str,list[200],tc,cur,hasil;

int main()
{
	scanf("%d",&tc);
	repp(t,1,tc)
	{
		scanf("%s",tmp);
		str=strlen(tmp);
		hasil=0;
		revv(y,str-1,0)
		{
			if(tmp[y]=='-')
			{
				hasil++;
				cur=0;
				if(tmp[0]=='+')
				{
					repp(x,0,str)
					{
						if(tmp[x]=='-')
						{
							//printf("beep%s\n",tmp);
							break;
						}
						
						else
						{
							tmp[x]='-';
						}
					}
					hasil++;
				}
				revv(z,y,0)
				{
					if(tmp[z]=='-')
					{
						list[z]=1;
					}
					else
					{
						list[z]=0;
					}
				}
				
				revv(z,y,0)
				{
					if(list[cur]==0)
					{
						tmp[z]='-';
					}
					else 
					{
						tmp[z]='+';
					}
					cur++;
				}
				
			}
			//printf("%s\n",tmp);
		}
		printf("Case #%d: %d\n",t,hasil);
	}
	return 0;
}
