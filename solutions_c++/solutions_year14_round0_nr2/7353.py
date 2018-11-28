// 

#define _CRT_SECURE_NO_WARNINGS 
#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <cmath>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <map>
#include <queue>
#include <set>
#include <queue>
#include <stack>
#include <deque>
#include <assert.h>
#include <ctime>
#include <bitset>
#include <numeric>
#include <complex>

using namespace std ;

int main()
{
  freopen("a.in","r",stdin);
  freopen("a.out","w",stdout);

   double t , c , f , x , y , T ;
   int count = 1 ;
   scanf("%lf",&t);

   while(t--)
   {
	   y = 2 , T = 0 ;

	   scanf("%lf%lf%lf",&c,&f,&x);

	   while(x/y >= x/(y+f)+c/y)
	   {
		   T+=(c/y);
		   y+=f ;
	   }
	   T+=(x/y);
	   printf("Case #%d: %0.7lf\n",count++,T);
   }
}