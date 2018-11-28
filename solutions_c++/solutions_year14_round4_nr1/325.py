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
int num[10011];
multiset<int>st;
int main()
{
	int T,cas=0;
	fop;
	scanf("%d",&T);
	while(T--)
	{
		st.clear();
		int n,x;
		scanf("%d%d",&n,&x);
		for(int i=0;i<n;i++)
		{
			scanf("%d",&num[i]);
			st.insert(num[i]);
		}
		int cnt=0;
		while(st.size()>0)
		{
			int now=*(--st.end());
			st.erase(st.find(now));
			multiset<int>::iterator it=st.upper_bound(x-now);
			if(st.size()==0||it==st.begin())
				cnt++;
			else
			{
				it--;
				st.erase(it);
				cnt++;
			}
		}
		printf("Case #%d: %d\n",++cas,cnt);
	}
}