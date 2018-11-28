#define _USE_MATH_DEFINES
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <set>
#include <vector>
#include <algorithm>
#include <queue>
#include <list>
#include <map>
#include <cmath>

using namespace std;

int main()
{
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	int T;
	cin >> T;
	for(int step=1; step<=T; ++step)
	{
		double C,F,X;
		cin >> C >> F >> X;
		double v=2;
		double ans=X/v;
		double time=0;

		while(time+C/v < ans)
		{
			time+=C/v;
			v+=F;
			ans=min(ans,time+X/v);
		}
		printf("Case #%d: %.9lf\n",step,ans);
	}
	//fclose(stdin);
	//fclose(stdout);
}
