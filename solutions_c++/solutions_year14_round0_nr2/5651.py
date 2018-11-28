#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <memory.h>
#include <string>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <queue>
#include <stack>
#include <map>
#include <vector>
#include <set>
#include <assert.h>

#define file_name ""

typedef long long ll;

const int N = 1e5+5;

using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int countTests;
	scanf("%d",&countTests);
	for(int numTest=1;numTest<=countTests;++numTest)
	{
		double c,f,x,ans = 1e9, curTime=0, add=2.0;
		scanf("%lf%lf%lf",&c,&f,&x);
		for(int i=0;i<100005;++i)
		{
			double d = x/add;
			if (ans > curTime + d)
				ans = curTime+d;
			curTime += c/add;
			add += f;
		}
		printf("Case #%d: %.7lf\n", numTest, ans);
	}
	return 0;
}
