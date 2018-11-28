#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<math.h>
using namespace std;
#define MAX(x,y) (x > y ? x : y)
#define MIN(x,y) (x > y ? y : x)

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin>>T;
	for (int idx = 1; idx <= T; idx++) {
		long double C,F,X;
		cin >> C >> F >> X;
		long double ret = 3.0 * X;
		long double d = 2.0;
		long double pot = 0.0;
		while(true)
		{
			if (X / d + pot < ret)
				ret = pot + X/d;
			pot += C / d;
			d+=F;
			if (pot > ret)
				break;
		}
		cout.precision(20);
		cout << "Case #"<< idx<< ": "<<ret<< endl;
	}
	return 0;
}