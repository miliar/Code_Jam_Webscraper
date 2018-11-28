#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>
#include <vector>
#include <sstream>
#include <stack>
#include <queue>
#include <map>
#include <climits>
#include <cstdio>
#include <set>
using namespace std;
#define db(a) (cout << (#a) << " = " << (a) << endl)
typedef long long ll;

int main()
{
  int T;
  cin>>T;
  for(int t=1;t<=T;t++)
  {
	double C,F,X;
	cin>>C>>F>>X;
	double c_f = 2.0;
	double c_t = 0.0;
	while(true)
	{
		double ttf1 = (X / c_f);
		double ttf2 = (C / c_f) + (X / (c_f + F));
		if(ttf1 <= ttf2)
		{
			c_t += ttf1;
			break;
		}
		c_t += (C / c_f);
		c_f += F;
	}
	cout << "Case #" << t << ": ";
	printf("%.7lf\n", c_t);
  }
  return 0;
}