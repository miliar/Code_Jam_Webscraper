#include <fstream>
#include <vector>
using namespace std;

void main() {
	ifstream in("A-large.in");
	ofstream out("out.txt");
	int t;
	in >> t;
	for (int i = 0; i < t; ++i) {
		int n;
		in >> n;
		out << "Case #" << i + 1 << ": ";
		if (n == 0) {
			out << "INSOMNIA" << endl;
			continue;
		}
		bool digits[10] = {};
		int cur = 0;
		while (1) {
			cur += n;
			int tmp = cur;
			do {
				digits[tmp % 10] = true;
				tmp /= 10;
			}while (tmp > 0);
			bool isfull = true;
			for (bool b : digits) {
				isfull &= b;
			}
			if (isfull) {
				out << cur << endl;
				break;
			}
		}
	}
	in.close();
	out.close();
}