#include <iostream>
#include <string>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>

#define type long long

using namespace std;

int main()
{

  cin.tie(NULL);
  std::ios::sync_with_stdio(false);

  int t;
  cin>>t;
  int cas = 1;
  while(t--)
  {

  	long double c,f,x;
  	long double t0 = 0.0;
  	cin>>c>>f>>x;
  	long double a = 2.0;
  	while(true)
  	{

  		if(x > (x*a)/(a+f) + c )
  		{
  			t0 += c/a;
  			a+=f;
  		}
  		else
  		{
  			t0 += x/a;
  			break;
  		}
  	}

  	cout.precision(20);
  	cout<<"Case #"<<cas<<": "<<t0<<"\n";
  	cas++;
  }

  return 0;
 
}