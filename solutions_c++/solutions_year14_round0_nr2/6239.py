#include <cstdlib>  
#include <cctype>  
#include <cstring>  
#include <cstdio>  
#include <cmath>  
#include <algorithm>  
#include <vector>  
#include <string>  
#include <iostream>  
#include <sstream>  
#include <map>  
#include <set>  
#include <queue>  
#include <stack>  
#include <fstream>  
#include <numeric>  
#include <iomanip>  
#include <bitset>  
#include <list>  
#include <stdexcept>  
#include <functional>  
#include <utility>  
#include <ctime>  
using namespace std;  

#define PB push_back  
#define MP make_pair  

#define REP(i,n) for(i=0;i<(n);++i)  
#define FOR(i,l,h) for(i=(l);i<=(h);++i)  
#define FORD(i,h,l) for(i=(h);i>=(l);--i)  
#define CLOCK cout << "Clock " << (double)clock()/CLOCKS_PER_SEC << endl
const double minv = 1e-9;
const int maxs = 1003;

int getN(double x,double c, double &delta)
{
	int res = 1;
	while ( (c*res-x)<=minv )
	{
		res ++;
	}
	res --;
	delta = x - res * c;
	return res;
}

double getSum(double c, double f, int n)
{
	double res = 0;
	for (int i=0;i<n; ++i)
		res += 1.0/(2+i*f);
	return res;
}

int main()
{
  freopen("B-large.in","r",stdin);
  freopen("B-large.out","w",stdout);
  int t;
  scanf("%d",&t);
  double c,f,x;
  for (int cases=1; cases<=t; ++cases)
  {
	  double res = 0;
	  cin >> c >> f >> x;
	  if (/*2-f>minv || */c-x>=minv)	res = x / 2;
	  else
	  {
	  	double delta = 0;
		int n = getN(x,c,delta);
		if (f-2>=minv)
		{
			if ((f*delta-2*c) > minv)
			{
				res = c * getSum(c,f,n);
				res += x / (2 + n*f);
			}
			else
			{
				res = c * getSum(c,f,n-1);
				res += x / (2 + (n-1)*f);
			}
		}
		else
		{
			if ((f * delta + (f - 2) * c) >= minv || n==1)
			{
				res =  c * getSum(c, f, n-1);
				res += x / (2 + (n - 1) * f);
			}
			else
			{
				res = c * getSum(c, f, n-2);
				res += x / (2 + (n - 2) * f);
			}
		}
	  }
	  printf("Case #%d: %.7lf\n",cases,res);
  }
  return 0;
}
