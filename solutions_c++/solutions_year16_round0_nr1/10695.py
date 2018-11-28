#include<iostream>
#include<fstream>
using namespace std;
ifstream f("counting.in");
ofstream g("counting.out");
int main() {
	long long N,S,A;
	bool ok;
	int T, v[11];
	f >> T;
	for (int k = 1; k <= T; k++) {
		f >> N;
		if (N == 0) {
			g << "Case #" << k << ": INSOMNIA\n";
		}
		else
		{
			S = 0;
			for (int i = 0; i < 10; i++)
				v[i] = 0;
			ok = 0;
			while (!ok) {
				S += N;
				ok = 1;
				A = S;
				while (A) {
					v[A % 10]++;
					A /= 10;
				}
				for (int i = 0; i < 10; i++)
					if (v[i] == 0) ok = 0;
			}
			g << "Case #" << k << ": " << S<<"\n";

		}	

	}
	system("pause");
	return 0;
}