#include <iomanip>
#include <algorithm>
#include <fstream>
#include <stack>
#include <queue>
#include <vector>
#include <map>
#include <cmath>
#include <iostream>
#include <string>
#include <set>

#define EPS 1e-7

using namespace std;

int main()
{
	int T;
	scanf("%d",&T);	
	int j = 0;
	for (int T_t = 1; T_t <= T; T_t++)
	{
		printf("Case #%d: ",T_t);
		double c,f,x,cp = 2.0,t = 0.0;
		scanf("%lf%lf%lf",&c,&f,&x);
		
		t = x / cp;
		double tt = 0.0;
		int i = 0;
		while (t - (tt + (c/cp) + x / (cp + f)) > EPS)
		{
			i++;
			t = tt + (c/cp) + (x / (cp + f));
			tt += c/cp;
			cp += f;
		};
		j = max(i,j);
		printf("%.7lf\n",t);
	}
//	cout << j << endl;
	return 0;	
}
