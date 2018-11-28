#include <fstream>
#include <set>
#include <string>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	ifstream in("input.txt");
	ofstream out("output.txt");
	int test;
	in >> test;
	for (int t = 1; t <= test; ++t) {
		out << "Case #" << t << ": ";
		long long n;
		in >> n;
		if (n == 0) {
			out << "INSOMNIA\n";
			continue;
		}
		set<char> seen;
		int i;
		for (i = 1; seen.size() < 10; ++i) {
			for (char c : to_string(i*n)) {
				seen.insert(c);
			}
		}
		out << (i - 1)*n << endl;
	}
}