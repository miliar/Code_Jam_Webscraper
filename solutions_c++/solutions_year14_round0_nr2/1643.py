#include <iostream>
#include <iomanip>

using namespace std;

int main(int argc, char const *argv[])
{
	ios::sync_with_stdio(0);

	int T;

	double Ta, Tb, Tc, Tt;
	double X;
	double C, F;
	int qtde;

	cin >> T;

	for (int z = 0; z < T; z++) {

		qtde = 0;
		Ta = Tb = Tc = Tt = 0;

		cin >> C >> F >> X;

//		Ta = X / (2 + (F * qtde));

		do {
			Ta = X / (2 + (F * qtde));

			Tb = C / (2 + (F * qtde));

			Tc = X / (2 + (F * (qtde + 1)));

			if (Ta < Tb + Tc) {
//				cout << Ta << " + ";
				Tt += Ta;
			}
			else {
//				cout << Tb << " + ";
				Tt += Tb;
			}

			qtde++;
		} while (Ta >= Tb + Tc);


		cout << "Case #" << z + 1 << ": " << fixed << setprecision(7) << Tt << '\n';
	}

	return 0;
}