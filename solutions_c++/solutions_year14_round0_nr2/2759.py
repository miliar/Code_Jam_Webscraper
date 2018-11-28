#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
#include <string.h>
#include <string>
#include <string>
#include <set>
#include <map>
#include <iomanip>

using namespace std;

double c, f, x, ans, pr;
void solve(int test)
{
	cin>>c>>f>>x;
	ans=0.0;
	pr=2.0;
	while (true)
	{
		long double t1, t2;
		t1=x/pr;
		t2=c/pr + x/(pr+f);
		if (t1<t2)
		{
			ans+=t1;
			break;
		}
		else
			ans+=c/pr, pr+=f;
	}
	printf("Case #%d: %.8lf\n", test, ans);
}
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int test;
	cin>>test;
	for (int i=1; i<=test; i++)
		solve(i);
	return 0;
}
