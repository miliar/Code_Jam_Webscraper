#include<iostream>
#include<fstream>
using namespace std;
int main() {
	ifstream input;
	input.open("input.txt");
	ofstream output;
	output.open("output.txt");
	int n;
	input >> n;
	for (int i = 0; i < n; i++) {
		int a, copy;
		input >> a;
		if (a == 0)
			output << "Case #" << i + 1 << ": INSOMNIA\n";
		else {
			int m = 1, z = 0, original = a, count[10];
			for (int j = 0; j < 10; j++)
				count[j] = 0;
			while (z == 0) {
				copy = original*m;
				a = copy;
				while (a > 0) {
					int d;
					d = a % 10;
					count[d]++;
					a = a / 10;
				}
				z = 1;
				for (int j = 0; j < 10; j++)
					z = z*count[j];
				if (z != 0)
					output << "Case #" << i + 1 << ": " << copy << "\n";
				m++;
			}
		}
	}
	input.close();
	output.close();
}