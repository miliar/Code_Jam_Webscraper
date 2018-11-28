#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <map>
#include <ctime>
#include <vector>
#include <string>

using namespace std;

typedef long long ll;

double C,F,X;

void get_ans()
{
	int n = (int)(ceil(X/C - 1 - 2/F) + 0.5);
	if(n < 0) n = 0;
	double ans = 0;
	double v = 2;
	for (int i = 0; i < n; ++i) {
		ans += C/v;
		v += F;
	}
	ans += X/v;
	printf("%.7lf\n", ans);
}
void read()
{
	cin >> C >> F >> X;
}

int main()
{
	int cas, tcas = 0;
	for (cin >> cas; cas; --cas)
	{
		read();
		printf("Case #%d: ", ++tcas);
		get_ans();
	}
}
