#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;

int main()
{
	ofstream of("a.txt");
	ifstream iff( "B-large.in",ios::in );

	int n;
	iff>>n;
	double C, F, X;

	for(int i=0;i<n;i++)
	{
		iff>>C>>F>>X;
		double t = 0;
		double u=2.0;
		double current = 0;
		bool flag=true;
		if(X<C)
		{
			t = X/2.0;
			flag = false;
		}
		while (flag)
		{
			t += C/u;
			current += C;
			if(current>=X)
			{
				t = t-(current-X)/u;
				break;
			}

			if( X/(u+F) <(X-C)/u)
			{
				current = 0;
				u += F;
			}
		}
		of<<"Case #"<<i+1<<": "<<setiosflags(ios::fixed)<<setprecision(7)<<t<<endl;
	}
	of.close();
	return 0;
}