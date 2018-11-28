#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

const int MAXN = 1000000;

int T;
double C, F, X;


double get_time(int n) 
{
	if (n == 0) return X / 2.0;

	double time = 0.0;
	double speed = 2.0;
	for (int i = 0; i < n; i++) 
	{
		time += C / speed;
		speed += F;
	}
 return time + X / speed;
}

int farm() 
{
	int l = 0, r = MAXN;
	while (r - l >= 3) 
	{
		int m1 = l + (r - l) / 3, m2 = r - (r - l) / 3;
		if (-get_time(m1) < -get_time(m2))
			l = m1;
		else
			r = m2;
	}
	double tmp = max(max(-get_time(l), -get_time(l+1)), -get_time(l+2));
	if (tmp == -get_time(l)) 
		return l;
	else 
		if (tmp == -get_time(l+1)) 
			return l+1;
		else 
			return l+2;
 
}

int main() 
{
#ifndef ONLINE_JUDGE
 freopen("input.txt", "r", stdin);
 freopen("output.txt", "w", stdout);
#endif
 cin >> T;
 for (int i = 1; i <= T; i++) 
 {
	cin >> C >> F >> X;
	printf("Case #%d: %.9f\n", i, get_time(farm()));
 }
 return 0;
}