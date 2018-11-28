#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,l,h) for(int i=(l);i<=(h);++i)
#define FORD(i,h,l) for(int i=(h);i>=(l);--i)

#define maxn 110
//#define maxm 1010
//#define maxk 1010

char a[maxn][maxn];

const int weiyi[4][2]={{-1,0},{1,0},{0,-1},{0,1}};
const char ch[4]={'^','v','<','>'};

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	
	int T;
	scanf("%d",&T);
	FOR(TT,1,T)
	{
		printf("Case #%d: ",TT);
		
		int n,m;
		cin>>n>>m;
		FOR(i,1,n)
			FOR(j,1,m)
				cin>>a[i][j];
		
		bool possible=true;
		int ans=0;
		FOR(i,1,n)
			FOR(j,1,m)
			{
				if (a[i][j]=='.') continue;
				bool flag=false;
				int d=0;
				FOR(k,0,3)
					if (a[i][j]==ch[k]) d=k;
				for(int i1=i+weiyi[d][0],j1=j+weiyi[d][1]; i1>=1&&i1<=n&&j1>=1&&j1<=m; i1+=weiyi[d][0],j1+=weiyi[d][1])
					if (a[i1][j1]!='.') flag=true;
				if (!flag)
				{
					ans++;
					FOR(k,0,3)
						for(int i1=i+weiyi[k][0],j1=j+weiyi[k][1]; i1>=1&&i1<=n&&j1>=1&&j1<=m; i1+=weiyi[k][0],j1+=weiyi[k][1])
							if (a[i1][j1]!='.') flag=true;
					if (!flag) possible=false;
				}
			}
		
		if (possible)
			cout<<ans<<endl;
		else
			cout<<"IMPOSSIBLE"<<endl;
	}
	
	return 0;
}
