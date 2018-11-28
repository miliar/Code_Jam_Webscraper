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

string problem_name = "B-small-attempt3";

void init(){
  freopen((problem_name+".in").c_str(),"rt",stdin);
  freopen((problem_name+".out").c_str(),"wt",stdout);
}



int main()
	
{
   init();


	int tst;
//	scanf("%d",&tst);
	scanf("%d\n",&tst);


	for (int cas = 1; cas<=tst;cas++)
	{
		int res = 0; 
		
		double V,X;

		int n;
		scanf("%d",&n);

		scanf("%lf%lf",&V,&X);

		double r1,c1,r2,c2;
		scanf("%lf%lf",&r1,&c1);
		

		if (n==2)
		{
			scanf("%lf%lf",&r2,&c2);			
			
		
		} else
		{
			r2 = 0;
			c2 = 0;
		}
		


		double l = 0,r=1e7;

		for (int step=1;step<100;step++)
		{
			double t = (l+r)/2;
		//	t = 50;
			double v1 = r1*t;
			double v2 = r2*t;
			if (v1+v2<V) 
			{
					l =t;
					continue;
			}

			double mnt ,mxt;
			if (c1<c2)
			{
				mnt = (min(v1,V)*c1 + ((V - min(v1,V))*c2))/V;
				mxt = (min(V,v2)*c2 + ((V - min(V,v2))*c1))/V;			
			} else
			{
				mnt = (min(V,v2)*c2 + ((V - min(V,v2))*c1))/V;
				mxt = (min(v1,V)*c1 + ((V - min(v1,V))*c2))/V;						
			}
			double a = mnt;
			double b = mxt;
			mnt = min(a,b);
			mxt = max(a,b);

			if (mnt-1e-11<=X && mxt+1e-11>=X) r=t; else l = t;		
		}




		if (l>=9*1e6) printf("Case #%d: IMPOSSIBLE\n",cas);	 else
		printf("Case #%d: %.9lf\n",cas,l);	

	}
	



	

	
   
	

   

	
  return 0;
}

