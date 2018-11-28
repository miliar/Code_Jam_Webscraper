#include <iostream>
#include <stdio.h>
#include <iomanip>
#include <fstream>
using namespace std;

int main()
{
	fstream in("test.in");
	fstream out("res.out");

	int T, k;
//	scanf("%d", &T);
	in>>T;
	double C, F, X;

	for (int i = 1; i <= T; i ++)
	{
//		cin>>C>>F>>X;
		in>>C>>F>>X;
		k = ceil((X * F - 2 * C - C * F) / (C * F));

		if (k <= 0)
		{
			out<<"Case #"<<i<<": "<<fixed<<setprecision(7)<<X/2<<endl;
//			cout<<"Case #"<<i<<": "<<fixed<<setprecision(7)<<X/2<<endl;
		}
		else
		{
			double res = X / (2 + k * F);
			for(int j = 1; j <= k; j ++)
			{
				res += C / (2 + (j - 1) * F);
			}
			out<<"Case #"<<i<<": "<<fixed<<setprecision(7)<<res<<endl;
//			cout<<"Case #"<<i<<": "<<fixed<<setprecision(7)<<res<<endl;
		}
	}
	return 0;
}