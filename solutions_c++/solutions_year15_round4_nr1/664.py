#include <stdio.h>
#include <sstream>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <list>
#include <iomanip>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <cassert>
#include <string.h>

using namespace std;
#pragma comment(linker, "/STACK:20000000")

typedef vector<int> vi; 
#define sz(a) int((a).size()) 
#define all(c) (c).begin(),(c).end() 

string problem_name = "A-large(4)";

void init(){
  freopen((problem_name+".in").c_str(),"rt",stdin);
  freopen((problem_name+".out").c_str(),"wt",stdout);
}

int colr[110],colc[110];
int u[110][110];

int main()
	
{
   init();


	int tst;
//	scanf("%d",&tst);
	scanf("%d\n",&tst);


	for (int cas = 1; cas<=tst;cas++)
	{
		int res = 0; 
		
		int r,c;
		char mas[110][110];

		memset(colc,0,sizeof(colc));
		memset(colr,0,sizeof(colr));
		memset(u,0,sizeof(u));

		scanf("%d %d\n",&r,&c);

		int f = 1;

		for (int i=0;i<r;i++) {
			gets(mas[i]);
			for (int j=0;j<c;j++) 
				if (mas[i][j]!='.') 
				{
					colr[i]++;
					colc[j]++;
				}
		}

		for (int i=0;i<r;i++)
		{
			for (int j=0;j<c;j++)
				if (mas[i][j]!='.')
				{					
					if (mas[i][j]=='<') res++;
					if (colr[i]==1 && colc[j]==1) f = 0;
					break;
				}	

			for (int j=c-1;j>=0;j--)
				if (mas[i][j]!='.')
				{					
					if (mas[i][j]=='>') res++;
					if (colr[i]==1 && colc[j]==1) f = 0;
					break;
				}		
		}

		
		for (int i=0;i<c;i++)
		{
			for (int j=0;j<r;j++)
				if (mas[j][i]!='.')
				{					
					if (mas[j][i]=='^') res++;
					if (colr[j]==1 && colc[i]==1) f = 0;
					break;
				}	

			for (int j=r-1;j>=0;j--)
				if (mas[j][i]!='.')
				{					
					if (mas[j][i]=='v') res++;
					if (colr[j]==1 && colc[i]==1) f = 0;
					break;
				}		
		}

		if (!f) printf("Case #%d: IMPOSSIBLE\n",cas);	 else
		printf("Case #%d: %d\n",cas,res);	

	}
	



	

	
   
	

   

	
  return 0;
}

