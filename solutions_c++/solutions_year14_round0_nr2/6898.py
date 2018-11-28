#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <memory.h>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <list>
#include <stack>
#include <set>
#include <map>

using namespace std;

vector<double> a;
int main()
{	
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int cases;
	cin>>cases;
	for (int curcase=1;curcase<=cases;curcase++)
	{
		cout<<"Case #"<<curcase<<": ";
		{
			double c,f,x;
			cin>>c>>f>>x;
			a.clear();
			a.push_back(0.0);
			double res = x/2;
			while (1)
			{
				double toget = a.back();
				double v = 2.0 + (a.size()-1)*f;
				double curt = c/v;
				double timetogetf = toget + curt;
				double newv = 2.0 +(a.size())*f;
				a.push_back(timetogetf);
				double restime = timetogetf + x/newv;
				if (restime<res)
				{
					res=restime;
				}
				else
					break;
			}
			printf("%.10lf",res);
		}
		cout<<"\n";
	}
	return 0;
}
