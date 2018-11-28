#include <cstdio>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <functional>
#include <limits>
#include <cassert>
#include <sstream>
#include <cmath>
#include <string>
#include <fstream>

using namespace std;
typedef long long ll;

const int max_n=100010;
const double eps=1e-12;

double C,F,X;
int T;

bool lt(double a, double b)
{
	return a+eps<b;
}

int main()
{
	scanf("%d",&T);
	for(int z=0; z<T; z++)
	{
		cin>>C>>F>>X;
		double S=2.0;
		double res=0.0;

		while(1)
		{
			double t1=X/S;
			double t2=C/S+X/(S+F);
			if(lt(t2,t1))
			{
				res+=C/S;
				S+=F;
			}
			else
			{
				res+=X/S;
				break;
			}
		}


		printf("Case #%d: ",z+1);
		printf("%.7f\n",res);
	}

	return 0;
}