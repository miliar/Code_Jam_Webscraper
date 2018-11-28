#include <fstream>

#define MAX 101
using namespace std;

ifstream in("input_a.txt");
ofstream out("output_a.txt");

long a, n;
long size[MAX];

long compute() {
	if (a == 1) {
		return n;
	}
	
	long count = 0, m;
	long long current_size = a, s;
	
	for (long i = 0; i < n; i++) {
		m = 0;
		s = current_size;

		while (s <= size[i]) {
			s = 2 * s - 1;
			m += 1;
		}

		if (m < (n - i)) {
			count += m;
			current_size = s + size[i];
		}
		else {
			return count + (n - i);
		}
	}
	return count;
}

int main() {
	long t;
	in >> t;
	
	for (long i = 0; i < t; i++) {
		in >> a >> n;
		
		for (long j = 0; j < n; j++) {
			in >> size[j];
		}
		
		sort(size, size + n);
		out << "Case #" << (i + 1) << ": " << compute() << endl;
	}
	return 0;
}