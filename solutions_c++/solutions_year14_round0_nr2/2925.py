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

string problem_name = "B-large";

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
		
		double c,f,x;
		scanf("%lf %lf %lf",&c,&f,&x);

		double res = x/2;

		double cur = 0;
		double cfarms = 0;
		double tottime = 0;
		for (int step=1;step<=50000000;step++)
		{
				double left = x - cur;
				double tm = left/(2+cfarms*f);
				if (tottime+tm<res) res = tottime+tm;

				left = c - cur;
				tm = left/(2+cfarms*f);
				tottime += tm;

				cur = 0;

				cfarms=cfarms+1;
		
		}


	
		printf("Case #%d: %.9lf\n",cas,res);
		
	}


	
  return 0;
}

