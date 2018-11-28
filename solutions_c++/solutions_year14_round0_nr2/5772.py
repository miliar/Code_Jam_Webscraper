#include <stdio.h>
#include <iostream>
#include <stack>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

int main()
{
	int t;
	int caso = 0;
	scanf(" %d ", &t);
	while(t--)
	{
		caso++;
		double c, f, x;
		scanf(" %lf %lf %lf ", &c, &f, &x);
		double resp = 0;
		double taxa = 2;
		while( (x - c)*(taxa + f) > taxa*x)
		{
			resp += c/taxa;
			taxa += f;
		}
		resp += x/taxa;
		printf("Case #%d: ", caso);
		printf("%.7lf\n", resp);
	}
}
