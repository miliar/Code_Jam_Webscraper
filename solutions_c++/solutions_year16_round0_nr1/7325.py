#include <fstream>
using namespace std;

bool f(bool b[10]) {
	for (int i = 0; i < 10; i++)
		if (!b[i]) return true;
	return false;
}
int main()
{
	ifstream in("A-large.in");
	ofstream out("A-large.out");
	int t;
	long long n, i = 1;
	in >> t;
	for (int j = 0; j < t; j++) {
		bool b[10];
		i = 1;
		for (int i = 0; i < 10; i++)
			b[i] = false;
		in >> n;
		if (n == 0) {
			out << "Case #" << j + 1 << ": INSOMNIA" << endl;
			continue;
		}
		while (f(b)) {
			long long x = i*n;
			while (x > 0) {
				b[x % 10] = true;
				x = x / 10;
			}
			i++;
		}
		out << "Case #" << j + 1 << ": " << (i - 1)*n << endl;
	}
	return 0;
}

