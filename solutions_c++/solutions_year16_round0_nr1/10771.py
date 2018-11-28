#include<iostream>
#include<fstream>
using namespace std;

unsigned long long int calculate(int, int);
void set(unsigned long long int);
void reset();
bool isOver();

bool check[10] = {0};
unsigned long long int  N[101];

int main() {
	unsigned long long int T, result;
	ifstream input;
	ofstream output;
	output.open("output.txt");
	input.open("A-large.in");

	input >> T;

	for (int i = 0; i < T; i++)
		input >> N[i];
	
	for (int i = 0; i < T; i++) {
		reset();
		result = calculate(i, 1);
		if (result != -1)
			output << "Case #" << i + 1 << ": " << result << endl;
		else
			output << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
	}

	input.close();
	output.close();
	return 0;
}

unsigned long long int calculate(int step, int mul) {
	if (mul >= 100)
		return -1;

	set(N[step] * mul);
	
	if(!isOver())
		return calculate(step, mul + 1);

	return N[step] * mul;
}

void set(unsigned long long int N) {
	if (N > 0) {
		check[N % 10] = true;
		set(N / 10);
	}
}

void reset() {
	for (int i = 0; i < 10; i++)
		check[i] = false;
}

bool isOver() {
	for (int i = 0; i < 10; i++)
		if (!check[i])
			return false;
	return true;
}