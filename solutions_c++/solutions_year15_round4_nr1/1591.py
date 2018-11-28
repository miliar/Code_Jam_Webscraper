#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#define PB push_back
#define MP make_pair
#define X first
#define Y second
#define lc (k<<1)
#define rc ((k<<1)|1)
#define mi ((l+r)>>1)
#define fk puts("fuck!")
using namespace std;
typedef long long ll;
typedef unsigned long long ull;

char mp[103][103];
int rowNum[103], colNum[103];
int visRowNum[103], visColNum[103];

int main()
{
	int cas;
	scanf("%d",&cas);
	for(int t=1;t<=cas;t++)
	{
		int r,c;
		scanf("%d%d",&r,&c);
		for(int i=0;i<r;i++)
			scanf("%s",mp[i]);
		bool ok=true;
		int ansCnt=0;
		// only one
		for(int i=0;i<r;i++) rowNum[i]=0, visRowNum[i]=0;
		for(int i=0;i<c;i++) colNum[i]=0, visColNum[i]=0;
		for(int i=0;i<r;i++)
			for(int j=0;j<c;j++)
				if(mp[i][j]!='.')
					rowNum[i]++, colNum[j]++;
		for(int i=0;i<r && ok;i++)
			for(int j=0;j<c && ok;j++)
				if(mp[i][j]!='.' && rowNum[i]==1 && colNum[j]==1)
					ok=false;
		printf("Case #%d: ",t);
		if(!ok)
		{
			puts("IMPOSSIBLE");
			continue;
		}
		// only one direction is one && other
		for(int i=0;i<r;i++)
			for(int j=0;j<c;j++)
				if(mp[i][j]!='.')
				{
					visRowNum[i]++, visColNum[j]++;
					bool still=false;
					if(colNum[j]>1)
					{
						if(visColNum[j]==1)	// only down
						{
							if(mp[i][j]=='v') still=true;
						}
						else if(visColNum[j]==colNum[j]) // only up
						{
							if(mp[i][j]=='^') still=true;
						}
						else
						{
							if(mp[i][j]=='^' || mp[i][j]=='v') still=true;
						}
					}
					if(rowNum[i]>1)
					{
						if(visRowNum[i]==1) // only right
						{
							if(mp[i][j]=='>') still=true;
						}
						else if(visRowNum[i]==rowNum[i]) // only left
						{
							if(mp[i][j]=='<') still=true;
						}
						else
						{
							if(mp[i][j]=='<' || mp[i][j]=='>') still=true;
						}
					}
					if(!still) ansCnt++;
				}
			printf("%d\n",ansCnt);
	}
	return 0;
}