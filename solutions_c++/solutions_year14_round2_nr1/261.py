#include <set>
#include <cmath>
#include <stack>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <numeric>
#include <vector>
#include <ctime>
#include <queue>
#include <list>
#include <map>
#define pi acos(-1.0)
#define INF 0x3f3f3f3f
#define clr(x)  memset(x,0,sizeof(x));
#define clrto(x,siz,y)  for(int xx=0;xx<=siz;xx++)  x[xx]=y;
#define clrset(x,siz)  for(int xx=0;xx<=siz;xx++)  x[xx]=xx;
#define clr_1(x) memset(x,-1,sizeof(x));
#define clrmax(x) memset(x,0x3f,sizeof(x));
#define clrvec(x,siz) for(int xx=0;xx<=siz;xx++)  x[xx].clear();
#define fop2   freopen(".in","r",stdin); //freopen(".out","w",stdout);
#define fop   freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
#define myprogram By_135678942570
#define clrcpy(x,siz,y)  for(int xx=0;xx<siz;xx++)  x[xx]=y[xx];
#define pb push_back
using namespace std;
string s[105];
int pos[106];
int main()
{
	fop
	int T,cas=0;
	scanf("%d",&T);
	while(T--)
	{
		clr(pos);
		int N;
		scanf("%d",&N);
		for(int i=0;i<N;i++)
			cin>>s[i];
		long long sum=0;
		printf("Case #%d: ",++cas);
		while(1)
		{
			int sizmax=0,sizmin=999;
			for(int i=0;i<N;i++)
			{
				sizmax=max((int)s[i].size()-pos[i],sizmax);
				sizmin=min((int)s[i].size()-pos[i],sizmin);
			}
			if(sizmax==sizmin&&sizmax==0)
			{
				printf("%d\n",sum);
				break;
			}
			else if(sizmin==0)
			{
				puts("Fegla Won");
				break;
			}
			char now=s[0][pos[0]];
			for(int i=0;i<N;i++)
				if(s[i][pos[i]]!=now)
				{
					puts("Fegla Won");
					goto loop;
				}
			if(0)
			{
				loop:;
				break;
			}
			vector<int>V;
			for(int i=0;i<N;i++)
			{
				int cnt=0;
				while(pos[i]<s[i].size()&&s[i][pos[i]]==now)
					pos[i]++,cnt++;
				V.pb(cnt);
			}
			sort(V.begin(),V.end());
			int need=V[V.size()/2];
			for(int i=0;i<V.size();i++)
				sum+=abs(need-V[i]);
		}
	}
}