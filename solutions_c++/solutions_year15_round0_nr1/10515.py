#include <string>
#include <iostream>
#include <cstdio>

using namespace std;

int solve(int,string);

int main()
{
	int T;
	cin >> T;

	int cs = 1;

	int sm;
	string ps;
	while(T--)
	{
		cin >> sm >> ps;
		int tinv = solve(sm,ps);
		printf("Case #%d: %d\n",cs,tinv);
		cs++;
	}
	return 0;
}

int solve(int sm, string ps)
{
	int toinvite = 0;
	int* q = new int[sm + 1];
	q[0] = ps[0] - '0';
	for(int i = 1; i <= sm; i++)
	{
		if(i <= q[i-1] || ps[i] == '0') q[i] = q[i-1] + ps[i] - '0';
		else
		{
			q[i] = i + ps[i] - '0';
			toinvite += i - q[i - 1];
		}
		if(q[i] >= sm) break;
	}
	delete[] q;
	return toinvite;
}
