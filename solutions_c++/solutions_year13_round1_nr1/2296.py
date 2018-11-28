#include <iostream>
#include <fstream>
#include <vector>
#include <map>

using namespace std;

//(2 * r + 2 * n - 1) * n <= m
int ringnums(int r, int m) {
        int n = 1;
        while (1) {
                int sum = (2 * r + 2 * n - 1) * n;
                if (sum == m) return n;
                else if (sum > m) return n - 1;
                n++;
        }
}

int main () {
	ifstream input;
	ofstream output;
	input.open("./A-small-attempt0.in");
	//input.open("./test.in");
	//output.open("./B-small-practice.out");
	output.open("./test.out");

	int t = 0;

	input >> t;
	int r, m;
	int n;
	for (int i = 0; i < t; i++) {
		input >> r >> m;
		n = ringnums(r, m);
		output << "Case #" << i + 1 << ": " << n << endl;
	}
	input.close();
	output.close();
	return 0;
}
