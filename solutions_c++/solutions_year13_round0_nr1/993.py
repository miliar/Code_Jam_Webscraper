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
#define pi acos(-1)
#define INF 0x7fffffff
#define clr(x)  memset(x,0,sizeof(x));
#define clrto(x,siz,y)  for(int xx=0;xx<=siz;xx++)  x[xx]=y;
#define clrset(x,siz)  for(int xx=0;xx<=siz;xx++)  x[xx]=xx;
#define clr_1(x) memset(x,-1,sizeof(x));
#define clrvec(x,siz) for(int xx=0;x<=siz;xx++)  x[xx].clear();
#define fop   freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
#define myprogram By_135678942570
#define clrcpy(x,siz,y)  for(int xx=0;xx<siz;xx++)  x[xx]=y[xx];
#define pb push_back
using namespace std;
int main()
{
	int t,cas=0;
	// fop;
	scanf("%d",&t);
	while(t--)
	{
		char mp[5][5]={0};
		for(int i=0;i<4;i++)
			scanf("%s",mp[i]);
		int fullfill=1;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				if(mp[i][j]=='.')
				{
					fullfill=0;
					break;
				}
		int sum1[333]={0};
		int sum2[333]={0};
		printf("Case #%d: ",++cas);
		for(int i=0;i<4;i++)
		{
			int sum11[333]={0};
			int sum22[333]={0};
			for(int j=0;j<4;j++)
				sum11[mp[i][j]]++,sum22[mp[j][i]]++;
			if(sum11['O']==4||sum11['O']==3&&sum11['T']==1||sum22['O']==4||sum22['O']==3&&sum22['T']==1)
			{
				printf("O won\n");
				goto loop;
			}
			if(sum11['X']==4||sum11['X']==3&&sum11['T']==1||sum22['X']==4||sum22['X']==3&&sum22['T']==1)
			{
				printf("X won\n");
				goto loop;
			}	
		}
		sum1[mp[0][0]]++,sum2[mp[0][0]]++;
		sum1[mp[1][1]]++,sum2[mp[1][1]]++;
		sum1[mp[2][2]]++,sum2[mp[2][2]]++;
		sum1[mp[3][3]]++,sum2[mp[3][3]]++;
		if(sum1['O']==4||sum1['O']==3&&sum1['T']==1||sum2['O']==4||sum2['O']==3&&sum2['T']==1)
		{
			printf("O won\n");
			goto loop;
		}
		if(sum1['X']==4||sum1['X']==3&&sum1['T']==1||sum2['X']==4||sum2['X']==3&&sum2['T']==1)
		{
			printf("X won\n");
			goto loop;
		}
		clr(sum1);clr(sum2);
		sum1[mp[0][3]]++,sum2[mp[0][3]]++;
		sum1[mp[1][2]]++,sum2[mp[1][2]]++;
		sum1[mp[2][1]]++,sum2[mp[2][1]]++;
		sum1[mp[3][0]]++,sum2[mp[3][0]]++;
		if(sum1['O']==4||sum1['O']==3&&sum1['T']==1||sum2['O']==4||sum2['O']==3&&sum2['T']==1)
		{
			printf("O won\n");
			goto loop;
		}
		if(sum1['X']==4||sum1['X']==3&&sum1['T']==1||sum2['X']==4||sum2['X']==3&&sum2['T']==1)
		{
			printf("X won\n");
			goto loop;
		}
		if(fullfill==0)
			puts("Game has not completed");
		else puts("Draw");
		loop:;
	}
}
