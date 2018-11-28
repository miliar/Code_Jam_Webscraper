#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
	int T;
	long double C, F, X, R, Tg, Tc, Tgc, Tt;
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
		R = 2.0;
		cin >> C >> F >> X;
		// printf("%.7Lf %.7Lf %.7Lf\n", C, F, X);
		Tc = 0.0; Tt = 0.0;
		do{
			Tt += Tc;
			Tg = X/R;
			Tc = C/R;
			Tgc = Tc + X/(R+F);
			R += F;
			// printf("Tt: %.7Lf Tg: %.7Lf Tc: %.7Lf Tgc: %.7Lf\n", Tt, Tg, Tc, Tgc);
		}
		while(Tgc < Tg);
		R -= F;
		Tt += Tg;

		cout << "Case #" << i+1 << ": ";
		printf("%.7Lf\n", Tt);
		// printf("%.7Lf %.7Lf %.7Lf\n", C, F, X);
	}
	return 0;
}