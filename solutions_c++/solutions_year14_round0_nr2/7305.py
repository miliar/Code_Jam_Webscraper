#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

void Open()
{
	freopen("P2.in", "r", stdin);
	freopen("P2.out", "w", stdout);
}

void Close()
{
	fclose(stdin);
	fclose(stdout);
}

void Run(int casenum)
{
	double C,F,X;
	cin >> C >> F >> X;
	double n = 1.0f;

	double lasttime = X / 2.f;
	double pasttime = 0.f;
	while (true)
	{
		pasttime = pasttime + C / (2.f + F * (n-1));
		double time = pasttime + X/(2.f + F * n);
		if (time > lasttime) break;
		n = n + 1;
		lasttime = time;
	}

	cout << "Case #" << casenum << ": ";
	printf ("%0.9lf\n", lasttime);
}

void Process()
{
	int casenum;
	cin >> casenum;
	for (int i = 1; i <= casenum; i++)
		Run(i);
}

int main()
{
	Open();
	Process();
	Close();
	return 0;
}