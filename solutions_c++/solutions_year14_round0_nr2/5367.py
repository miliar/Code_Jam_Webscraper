#include<iostream>
#include<cstdio>

using namespace std;

void solve(double C, double F, double X)
{
	double T[100000];
	T[0] = 0;
	for(int i = 1; ; i++)
	{
		T[i] = T[i-1] + C/((i-1)*F + 2.0);
		if(T[i] + X/(i*F + 2.0) > T[i-1] + X/((i-1)*F+2.0))
		{
			double A = T[i-1] + X/((i-1)*F+2.0);
			printf("%0.7lf\n", A);
			break;
		}
	}
}

int main(void)
{
	freopen("BL.in", "r", stdin);
	freopen("BL.out", "w", stdout);
	double C, F, X;
	int t = 1, T, N;
	cin>>T;
	while(T--)
	{
		cin>>C>>F>>X;
		cout<<"Case #"<<t++<<": ";
		solve(C, F, X);
	}
	return 0;
}
