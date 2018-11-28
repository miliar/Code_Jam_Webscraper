#include <fstream>
#include <vector>
#include <string>
using namespace std;

void main() {
	ifstream in("D-small-attempt0.in");
	ofstream out("out.txt");
	int t;
	in >> t;
	for (int i = 0; i < t; ++i) {
		long long k, c, s, kc;
		in >> k >> c >> s;
		out << "Case #" << i + 1 << ": ";
		kc = 1;
		for (int j = 0; j < c - 1; ++j) {
			kc *= k;
		}
		for (int j = 0; j < s; ++j) {
			out << kc * j + 1 << " "; 
		}
		out << endl;
	}
	in.close();
	out.close();
}