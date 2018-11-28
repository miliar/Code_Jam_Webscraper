#include <iostream>
using namespace std;


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	long double C,F,X;
	double s;
	int n;
	cin>>T;

	for(int i = 0; i < T; ++i)
	{
		cin>>C>>F>>X;
		
		s = 0.0;
		n = (long double)(  ((F*X)/C - 2 ) / F );

		if( n < 0 )
			n = 0;

		for(int tmp = 0 ; tmp < n; ++ tmp)
			s += C/(2+tmp*F)  ;
		s += X/(2+(double)n*F);

		cout.setf(ios::fixed);
		cout.precision(7);
		cout << "Case #" << i+1 << ": "<<s<<endl;
	}


	return 0;
}