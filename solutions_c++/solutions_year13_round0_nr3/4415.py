#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

using namespace std;

bool isFair(int n) {
	if (n < 10) return true;
	int p = n;
	int t = 0;

	while (p > 0) {
		t = t * 10 + (p % 10);
		p = p / 10;
	}

	return n == t;
}

int fsnumber(int a, int b) {
	int sum = 0;
	int squa = (int)sqrt((double)a);
	int i = a;
	
	if (squa * squa >= a)
		i = squa;
	else
		i = squa + 1;

	while (1) {
		squa = i * i;
		if (squa > b) break;
		if (isFair(i) && isFair(squa)) sum++;
		i++;
	}

	return sum;
}

int main () {
	ifstream input;
	ofstream output;
	input.open("./C-small-attempt0.in");
	//input.open("./test.in");
	//output.open("./B-small-practice.out");
	output.open("./test.out");

	int t = 0;

	input >> t;
	int a, b;
	int res;
	for (int i = 0; i < t; i++) {
		input >> a >> b;
		res = fsnumber(a, b);
		cout << a << " : " << b << endl;
		output << "Case #" << i + 1 << ": " << res << endl;
	}
	input.close();
	output.close();
	return 0;
}