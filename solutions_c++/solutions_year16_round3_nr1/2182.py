#include <fstream>
#include <iostream>

using namespace std;

void evaluate(int p[], int N, ofstream &out);
int getSum(int p[], int N);
bool outputOver(int p[], int N, int over, ofstream &out);

int main() {
	//set input/output stream
	ifstream input;
	ofstream output;
	input.open("input.txt");
	output.open("output.txt");

	int T;
	int N;
	int p[50];

	input >> T;
	for(int x = 1; x <= T; x++) {
		input >> N;
		for(int i = 0; i < N; i++) {
			input >> p[i];
		}

		output << "Case #" << x << ": ";
		evaluate(p, N, output);
		output << endl;
	}
	return 0;
}

void evaluate(int p[], int N, ofstream &out) {
	int sum = getSum(p, N);
	if(sum == 0) {
		return;
	}
	int over = (sum - 1) / 2 + 1;
	if(outputOver(p, N, over, out) == false) {
		for(int i = 0; i < N; i++) {
			if(p[i] > 0) {
				char ch = 'A' + i;
				p[i]--;
				out << ch;
				break;
			}
		}
	}
	out << ' ';
	evaluate(p, N, out);
}

int getSum(int p[], int N) {
	int sum = 0;
	for(int i = 0; i < N; i++) {
		sum += p[i];
	}

	return sum;
}

bool outputOver(int p[], int N, int over, ofstream &out) {
	bool ret = false;
	for(int i = 0; i < N; i++) {
		if(p[i] >= over) {
			char ch = 'A' + i;
			p[i]--;
			out << ch;
			ret = true;
		}
	}

	return ret;
}
