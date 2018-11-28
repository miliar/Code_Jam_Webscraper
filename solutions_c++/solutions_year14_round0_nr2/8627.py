#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>
#include <map>
#include <set>
#include <algorithm>
#include <cstring>
#include <queue>
#include <stack>
#include <cmath>
#include <sstream>
#include <cstdio>
#include <ctime>

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VII;

typedef long long llong;

int main()
{
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);

  int TC;
  cin>>TC;

  for(int j = 1; j <= TC; j++)
  {
  	double buy, bonus, goal;

  	cin>>buy>>bonus>>goal;

  	double cookies = 0, rate = 2;
  	int counter = 100000000;
  	double ans = 1000000;
  	double totaltime = 0;

  	while(counter--)
  	{	

  		double cookiesforTotal = goal - cookies;
  		double cookieforFactory = buy - cookies;
  		double timeforTotal = totaltime + cookiesforTotal/rate;

  		double timeforFactory = cookieforFactory/rate;
  		totaltime += timeforFactory;
  		rate+=bonus; 

  		ans = min(timeforTotal,	ans);
  	}

  	printf("Case #%d: %.7f\n", j, ans);

  }
  
  return 0;
}



