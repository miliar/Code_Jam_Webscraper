#include <iostream>
#include <fstream>
using namespace std;


int T;

int main()
{
	ifstream in("cs.in");
	ofstream out("cs.out");
	in >> T;
	for (int i = 0; i < T; i++) {
		int N; in >> N;
		if (N == 0) out << "Case #" << (i+1) << ": INSOMNIA\n";
		else {
			int seen = 0; int mult = 1;
			while (seen != (1 << 10) - 1) {
				long long k = N*mult;
				while (k > 0) {
					seen |= (1 << (k % 10));
					k /= 10;
				}
				mult++;
			}

			out << "Case #" << (i+1) << ": " << (mult - 1)*N << "\n";
		}
	}
	in.close();
	out.close();

	return 0;
}