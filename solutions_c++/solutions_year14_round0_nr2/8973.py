#include <iostream>
#include <sstream>
#include <fstream>
#include <stdio.h>
#include <numeric>
#include <vector>
#include <string>
#include <math.h>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <stdio.h>
#include <string.h>
#include <tuple> 
#include <iomanip>
using namespace std;


int main(int argc, const char **argv) 
{	
	freopen("B-small-attempt0.in","r",stdin);
	freopen("Cookie Clicker Alpha.out","w",stdout);
	int T;
	double C, X, secs = 0.0, F, buyF, rate, total;
	cin>>T;
	for (int i = 0; i < T; i++)
	{
		total = 0.0;
		cin>>std::dec>>C>>F>>X;
		rate = 2.0000000000000;
		secs = X/rate;
		while (true)
		{
			buyF = C / rate;
			rate+=F;
			total += buyF;
			total += (X/rate);
			if (secs < total)
			{
				break;
			}
			secs = total;
			total-= (X/rate);
		}
		cout<<"Case #"<<i+1<<": ";
		printf("%.7f\n",secs);
	}

	return 0;
}
