/* Problem B. Cookie Clicker Alpha */

/*
	We could use Geometric Sequences with combination on Binary Search
	n = X
		=> O(log n)
	but instead I will just start with farm = 0 and look for the climax
		=> O(n)
*/

#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <deque>
#include <stack>
#include <queue>
#include <algorithm>

using namespace std;

int n;
double c, f, x;

int main(){
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);

	scanf("%d", &n);

	for (int i = 0; i < n; ++i)
	{
		scanf("%lf %lf %lf", &c, &f, &x);
		double res = 0;
		double last = x/2;
		int j=0;	// farm number
		double s = 0;
		while(true){
			if (j!=0) res = res + c/(2+f*(j-1));
			s = x/(2+f*j);
			if ((res+s)>last)
			{
				break;
			}else{
				last = res+s;
			}
			j++;
		}

		printf("Case #%d: %.7lf\n", i+1, last);
	}

	return 0;
}







