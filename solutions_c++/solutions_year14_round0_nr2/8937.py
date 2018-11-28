#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<cmath>
#include<string>
#include<cstdio>
#include <stdio.h>
#include<sstream>
#include<map>
#include<list>
#include<queue>
#include<set>
#include<numeric>
using namespace std;
int main()
{
   long double c,f,x;
   long double ns,t1,t2,p;
   int t;
   cin>>t;
   for (int k = 0; k < t; k++)
   {
	   cin>>c>>f>>x;
	   ns=0;
	   p=2;
	   if (x<=c)
	   ns=x/2.0;
	   else
		   while(1)
	   {
		   t1=x/p;
		   t2=(c/p)+(x/(p+f));
		   if (t1<=t2)
		   { ns+=t1; break; }
		   else
		   {
			   ns+=(c/p);
			   p=p+f;
		   }
	   }
		   printf("Case #%d: %.7lf\n",k+1,ns);
   }
   return 0;
}