#include<fstream>
using namespace std;

int main() {

	ifstream fin("input.in");
	ofstream fout("input.out");

	int test;
	fin >> test;
	for (int i = 0; i < test; i++) {

		int n;
		fin >> n;

		if (n == 0) {
			fout << "Case #" << (i + 1) << ": INSOMNIA\n";
			continue;
		}

		bool used[10] = { false, false, false, false, false, false, false, false, false, false};
		int count = 10;

		int add = n;
		n = 0;

		while (count) {
			n += add;
			int buf = n;

			while (buf) {
				if (!used[buf % 10]) {
					count--;
					used[buf % 10] = true;
				}

				buf /= 10;
			}
		}

		fout << "Case #" << (i + 1) << ": " << n << endl;

	}

	return 0;
}