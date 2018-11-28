#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>

#include<cmath>
#include<iostream>
#include<iomanip>
#include<fstream>

#include<string>
#include<utility>
#include<vector>
#include<list>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
#define ii long long int
#define pi 2*acos(0.0)
#define eps 1e-7
#define mem(x,y) memset(x,y,sizeof(x))
#define all(x) x.begin(), x.end()
#define pb push_back
#define sz(a) (int)a.size()
#define inf 2147483640

#define mx 100010
#define r 4
#define c 4

using namespace std;

const int debug= 0;
char s[5][5];

bool empty()
{
	for (int i=0;i<r;++i) for (int j=0;j<c;++j) if (s[i][j]=='.') return 1;
	return 0;
}

bool row(int i,char ch)
{
	if (ch=='.') return 0;
	int j;
	for (j=0;j<c;++j)
	{
		if (s[i][j]==ch || s[i][j]=='T') continue;
		else return 0;
	}
	return 1;
}

bool col(int j,char ch)
{
	if (ch=='.') return 0;
	int i;
	for (i=0;i<r;++i)
	{
		if (s[i][j]==ch || s[i][j]=='T') continue;
		else return 0;
	}
	return 1;
}

bool diagonal(int i,int dx,int dy,char ch)
{
	if (ch=='.') return 0;
	int x= i,y= 0;
	while (1)
	{
		if (x<0 || x==r || y<0 || y==c) break;
		if (s[x][y]==ch || s[x][y]=='T')
		{
			x+= dx,y+= dy;
			continue;
		}
		else return 0;
		
	}
	return 1;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,x;
	scanf("%d",&t);
	
	for (x=1;x<=t;++x)
	{
		int i;
		for (i=0;i<r;++i) scanf("%s",s[i]);
		bool found= 0,has= empty();
		char ch,cc;
		
		for (i=0;i<r;++i)
		{
			if (s[i][0]=='.') continue;
			if (s[i][0]=='T') cc= s[i][3];
			else cc= s[i][0];
			
			found= row(i,cc);
			if (found)
			{
				ch= cc;
				break;
			}
		}
		
		if (!found)
		{
			for (i=0;i<c;++i)
			{
				if (s[0][i]=='.') continue;
				if (s[0][i]=='T') cc= s[3][i];
				else cc= s[0][i];
				
				found= col(i,cc);
				if (found)
				{
					ch= cc;
					break;
				}
			}
		}
		
		if (!found)
		{
			if (s[0][0]=='T') cc= s[3][3];
			else cc= s[0][0];
			found= diagonal(0,1,1,cc);
			if (found)
			{
				ch= cc;
			}
		}
		
		if (!found)
		{
			if (s[3][0]=='T') cc= s[0][3];
			else cc= s[3][0];
			found= diagonal(3,-1,1,cc);
			if (found)
			{
				ch= cc;
			}
		}
		
		printf("Case #%d: ",x);
		if (found) {printf("%c won\n",ch);continue;}
		if (has) puts("Game has not completed");
		else puts("Draw");
	}
	
	return 0;	
}
