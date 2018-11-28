#include <iostream>
#include <fstream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <stdio.h>
#include <cmath>
#include <math.h>
#include <stdlib.h>

#include <algorithm>
#include <cstring>
#include <vector>
#include <string>
#include <sstream>
#include <queue>
using namespace std;
int main()
{
	int T;
	double C,F,X;
	scanf("%d",&T);
	for (int i=1;i<=T;i++)
	{
		scanf("%lf%lf%lf",&C,&F,&X);
		double last_time = X/2;
		double new_time = X/(2+F)+C/2;
		int farm = 1;
		while(new_time<last_time)
		{
			last_time = new_time;
			new_time = new_time - X/(2+F*farm) + X/(2+F*(farm+1)) + C/(2+farm*F);
			farm++;
		}
		printf("Case #%d: %.7lf\n",i,last_time);

	}
	return 0;
}