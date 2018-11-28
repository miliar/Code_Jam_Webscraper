#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
	int T = 0;
	cin >> T;
	for (int i=1;i<=T;++i)
	{
		double C = 0;
		double F = 0;
		double X = 0;
		
		cin >> C >> F >> X;
		
		
		int t = 0;
		while ( (C/(2+F*t)+X/(2+F*(t+1))) < X/(2+F*t) )
		{
			++t;
		}
		
		double rst = 0.0000000;
		int k = 0;
		for (int j=0;j<t;++j)
		{
			
			rst = rst + C/(2+F*k);
			++k;
		}
		rst = rst + X/(2+F*t);
		cout <<"Case #"<<i<<": "<< setiosflags(ios::fixed) << setprecision(7)<<rst<<endl;
	}
	
}