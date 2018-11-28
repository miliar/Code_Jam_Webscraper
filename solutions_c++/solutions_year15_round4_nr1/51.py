#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <list>
#include <queue>
#include <vector>
#include <ctime>
#include <set>
#include <bitset>
#include <deque>
#include <fstream>
#include <stack>
#include <map>
#include <utility>
#include <cassert>
#include <string>
#include <iterator>
#include <cctype>
using namespace std;
typedef long long LL;
double getd()
{
    double d=0,d2=0,d3=1; char ch; bool flag=0;
    while(!isdigit(ch=getchar()))if(ch=='-')break;
    if(ch=='-')flag=true;else d=ch-48;
    while(isdigit(ch=getchar()))d=d*10+ch-48;
    if(ch=='.')
    {
        while(isdigit(ch=getchar()))d2=d2*10+ch-48,d3=d3*0.1;
        d+=d3*d2;
    }
    if(flag)return -d;else return d;
}
int get()
{
    int f=0,v=0;char ch;
    while(!isdigit(ch=getchar()))if(ch=='-')break;
    if(ch=='-')f=1;else v=ch-48;
    while(isdigit(ch=getchar()))v=v*10+ch-48;
    if(f==1)return -v;else return v;
}
char a[1000][1000];
const int dx[]={0,0,1,-1};
const int dy[]={1,-1,0,0};
int main()
{
	freopen("AL.in","r",stdin);
	freopen("AL.out","w",stdout);
	int T=get();
	for(int _=1;_<=T;_++)
	{
		int n=get(),m=get();
		for(int i=1;i<=n;i++)
			for(int j=1;j<=m;j++)scanf(" %c",&a[i][j]);
		bool have=1;int ans=0;
		for(int i=1;i<=n;i++)
			for(int j=1;j<=m;j++)
			{
				int d;
				if(a[i][j]=='<')d=1;
				else if(a[i][j]=='^')d=3;
				else if(a[i][j]=='>')d=0;
				else if(a[i][j]=='v')d=2;
				else continue;
				int x=i,y=j;
				bool ok=0;
				x+=dx[d],y+=dy[d];
				while(1<=x&&x<=n&&1<=y&&y<=m)
				{
					if(a[x][y]!='.'){ok=1;break;}
					x+=dx[d],y+=dy[d];
				}
				if(ok)continue;
				for(int k=1;k<i;k++)
					if(a[k][j]!='.')ok=1;
				for(int k=i+1;k<=n;k++)
					if(a[k][j]!='.')ok=1;
				for(int k=1;k<=m;k++)
					if(k!=j&&a[i][k]!='.')ok=1;
				if(ok)ans++;else have=0;
			}
		if(have)printf("Case #%d: %d\n",_,ans);
		else printf("Case #%d: IMPOSSIBLE\n",_);
	}
	return 0;
}
