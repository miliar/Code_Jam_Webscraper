#include <iostream>
#include <cstdio>
using namespace std;

double solve( double now , double C, double F, double X )
{
	//cout << now << " " << C << " " << F << " " << X << endl;
	if( (X/now) < ( C/now + X/(now+F)) )
		return X/now;	

	double ats = solve( now+F , C,F,X );

	if( (X/now) < ( C/now + ats)  )
		return (X/now);
	return C/now + ats;
}

int main()
{
	int T;
	cin >> T;
	for(int cas=1;cas<=T;cas++)
	{
		double C,F,X;
		cin >> C >> F >> X;
		printf("Case #%d: %lf\n",cas,solve(2.0,C,F,X));
	}
	return 0;
}