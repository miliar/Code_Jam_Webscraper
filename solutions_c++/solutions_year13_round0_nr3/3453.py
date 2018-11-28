#include <fstream>
using namespace std;

ifstream in("input_c.txt");
ofstream out("output_c.txt");

int a, b;
int pal[] = {1, 4, 9, 121, 484};

int compute() {
	int count = 0;
	for (int i = 0; i < 6; i++) {
		if (pal[i] >= a && pal[i] <= b) {
			count += 1;
		}
	}
	return count;
}

int main() {
	int t;
	in >> t;
	
	for (int i = 0; i < t; i++) {
		in >> a >> b;
		out << "Case #" << (i + 1) << ": " << compute() << endl;
	}
	return 0;
}
