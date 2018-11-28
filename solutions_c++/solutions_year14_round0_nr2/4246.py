#include <iostream>
#include <cmath>
using namespace std;
int main()
{
	int T;
	cin >> T;
	for(int i=1; i<=T; i++)
	{
		double C,F,X;
		cin >> C>>F>>X;
		int I = ceil((X*F - C*F - 2*C )/ (C*F));
		if(I < 0) I = 0;
		double t= 0;
		for (int j = 0; j<I; j++)
		{
			t = t + C / (2 + j * F);
		}
		t = t + X / (2  + I*F);
		cout.precision(7);
		cout << "Case #"<<i<<": "<<fixed<<t<<endl;
	}
}
