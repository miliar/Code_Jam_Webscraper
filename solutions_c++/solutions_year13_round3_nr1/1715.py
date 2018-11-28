#include <fstream>
#include <algorithm>
#include <cmath>
#include <string>

using namespace std;

ifstream in("input_a.txt");
ofstream out("output_a.txt");

long n;
string s;

bool cons(char c) {
	return c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u';
}

long compute() {
	long total = 0;
	long length = s.size();

	for (long i = 0; i < length; i++) {
		for (int j = i + 1; j <= length; j++) {
			long count = 0;

			for (int k = i; k < j; k++) {
				if (cons(s[k])) {
					count += 1;
					if (count == n) {
						total += 1;
						break;
					}
				}
				else {
					count = 0;
				}
			}
		}
	}
	return total;
}

int main() {
	int t;
	in >> t;
	for (int i = 0; i < t; i++) {
		in >> s >> n;
		out << "Case #" << (i + 1) << ": " << compute() << endl;
	}
}