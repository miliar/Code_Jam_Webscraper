#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<vector>
#include<cstring>
using namespace std;

double C, F, X;

void Input()
{
	cin>>C>>F>>X;
}

void Solve(int t)
{
	double time = 0.0;
	double R = 2.0;
	while (X / R > C / R + X / (R + F)) {
		time += C / R;
		R += F;
	}
	time += X / R;
	//cout<<"Case #"<<t<<": "<<time<<endl;
	printf("Case #%d: %.7f\n", t, time);
}

int main()
{
	int T;
	cin>>T;
	for (int i = 1; i <= T; i++) {
		Input();
		Solve(i);
	}
	return 0;
}
