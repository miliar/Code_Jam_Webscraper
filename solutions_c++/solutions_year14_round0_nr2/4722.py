#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>
#include <cstdio>

using namespace std;

int main()
{
     int T,cas=1;
     cin >> T;
     while(T--)
     {
	cout << "Case #" << cas <<": ";
	cas++;
	double C,F,X;
	cin >> C >> F >> X;
	double rate = 2.0,var = 0.0;
	double prev,cur;
	cur = X;
	cur = cur/rate;
	while(1)
	{
	   prev = cur;
	   cur = C;
	   cur = C/rate;
	   var += cur;
	   rate = rate+F;
	   cur = X/rate;
	   cur += var;
	   if(cur-prev > 0.0000001)
		 break;	
	}
	printf("%.7lf\n",prev);
     }
   return 0;
}
