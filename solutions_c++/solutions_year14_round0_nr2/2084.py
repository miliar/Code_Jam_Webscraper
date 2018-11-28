#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <cstring>
#include <fstream>

using namespace std;

int main()
{

	freopen("input.txt","r",stdin);

	int T;
	scanf("%d",&T);

	for(int t=1;t<=T;t++)
	{
		printf("Case #%d: ",t);
		double C, F, X;
		scanf("%lf %lf %lf",&C,&F,&X);
		double y = (X*F-2.0*C)/(C*F);
		int n = y;
		n = max(n,0);
		double ans = X/(2.0+(double)n*F);
		for(int i=1;i<=n;i++)
			ans += C/(2.0+(double)(i-1)*F);
		printf("%0.7lf\n",ans);
	}

	return 0;

}
