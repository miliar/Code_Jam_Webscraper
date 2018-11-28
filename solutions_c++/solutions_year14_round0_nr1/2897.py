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
#include "windows.h"
using namespace std;
#pragma comment(linker, "/STACK:20000000")

typedef vector<int> vi; 
#define sz(a) int((a).size()) 
#define all(c) (c).begin(),(c).end() 

string problem_name = "A-small-attempt0";

void init(){
  freopen((problem_name+".in").c_str(),"rt",stdin);
  freopen((problem_name+".out").c_str(),"wt",stdout);
}


int mas[4][4];

int main()
{
   init();

	int tst;
	scanf("%d",&tst);

	for (int cas = 1; cas<=tst;cas++)
	{
		int r;
		scanf("%d",&r);
		set <int> s;
		for (int i=0;i<4;i++)
		for (int j=0;j<4;j++)
		{
			scanf("%d",&mas[i][j]);
			if (i==r-1) s.insert(mas[i][j]);		
		}	

		scanf("%d",&r);
		//set <int> s;
		int res = -1;
		int ok = 1;
		for (int i=0;i<4;i++)
		for (int j=0;j<4;j++)
		{
			scanf("%d",&mas[i][j]);
			if (i==r-1) 
			{
				if (s.find(mas[i][j])!=s.end())
				{
					if (res!=-1) ok=0;
					res = mas[i][j];
				}
			}
		}	
			
	
		printf("Case #%d: ",cas);
		if (res==-1)
			printf("Volunteer cheated!\n"); else
		if (ok==0)
			printf("Bad magician!\n"); else
			printf("%d\n",res);

	}


	
  return 0;
}

