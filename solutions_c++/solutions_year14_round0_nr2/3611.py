#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
double eps=0.00000001;
using namespace std;
int main()
{
	freopen("bs.in","r",stdin);
	freopen("b_small.out","w",stdout);
	int t;
	cin>>t;
	for(int testc=1;testc<=t;testc++)
	{
		double c,f,x,rate=2.0,cookie_count=0,curr_time=0;
		cin>>c>>f>>x;
		while(c<x-c-eps)
		{
			if(x/(rate+f)<((x-c)/rate)-eps)
			{
				curr_time+=(c/rate);
				cookie_count=0;
				rate+=f;
			}
			else
				break;
		}
		curr_time+=(x-cookie_count)/rate;
		cout.precision(7);
		cout<<"Case #"<<testc<<": "<<fixed<<curr_time<<"\n";
	}
	return 0;
}