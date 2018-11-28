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

using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int i,j,k,t,n,cases;
	double C,F,X,f,maxsum,sum,ans;
	scanf("%d",&t);
	for(cases=1;cases<=t;cases++)
	{
		scanf("%lf%lf%lf",&C,&F,&X);
		f=2.0;
		sum = 0.0;
		ans = (double)10000000.0;
		maxsum = (double)X/2;
		while(1)
		{
			double cursum = sum+(double)X/f;
			if(cursum>ans) break;
			else
				ans = cursum;	
			sum+=(double)C/f;
			f+=F;
		}
		printf("Case #%d: %.7lf\n",cases,ans);	
	}
	
	return 0;
}