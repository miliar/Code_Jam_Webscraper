#include <iostream>
#include <sstream>
#include <functional>
#include <climits>
#include <cstddef>
#include <numeric>
#include <string>
#include <string.h>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>
#include <set>
#include <map>

using namespace std;
typedef long long ll;


int main()
{
	int T;cin>>T;
	for (int CASE = 1; CASE <= T; CASE++)
	{
		double C,F,X;cin>>C>>F>>X;

		double time=0.0,ans=X/2.0;
		for (int i = 0; i < 200000; i++)
		{
			double cur=2.0+i*F;
			ans=min(ans,time+X/cur);
			time+=C/cur;
		}

		printf("Case #%d: %.8f\n",CASE,ans);
	}
	return 0;
}