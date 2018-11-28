#include <fstream>
#include <iostream>
#include <bitset>
#include <math.h>
using namespace std;

#define BIT_NUM 16

int N, J;

int solution[500][9];
bitset<BIT_NUM> solbit[500];

inline long long convert_base(bitset<BIT_NUM> now, int base) {
	long long ret = 0;
	for (int i = N - 1; i >= 0; i--) {
		ret *= base;
		ret += now[i];
	}
	return ret;
}

inline int check_prime(long long num) {
	long long for_max = sqrt(num);
	for (long long i = 2; i <= for_max; i++) {
		if (num % i == 0)
			return i;
	}
	return -1;
}

void run() {
	int now_solution[9];
	bitset<BIT_NUM> now_bit;
	long long now_num;
	int div;

	bool answer;
	int answer_count = 0;

	for (long long i = ((long long)1 << (N-1)) + 1; i < ((long long)1 << N); i = i + 2) {
		now_bit = bitset<BIT_NUM>(i);
		answer = true;
		for (int base = 2; base <= 10; base++) {
			now_num = convert_base(now_bit, base);
			div = check_prime(now_num);
			if (div == -1) {
				answer = false;
				break;
			}
			else {
				now_solution[base - 2] = div;
			}
		}
		if (answer) {
			solbit[answer_count] = now_bit;
			for (int i = 0; i < 9; i++)
				solution[answer_count][i] = now_solution[i];
			answer_count++;
			if (answer_count >= J)
				return;
		}
	}
}

int main() {
	int T;
	ifstream in("C-small-attempt0.in");
	ofstream out("output.txt");
	in >> T;
	for (int t = 0; t < T; t++) {
		//read file
		in >> N >> J;
		//run
		run();
		//output
		out << "Case #" << t + 1 << ":" << endl;
		for (int i = 0; i < J; i++) {
			out << solbit[i] << ' ';
			for (int j = 0; j < 9; j++)
				out << solution[i][j] << ' ';
			out << endl;
		}
	}
	in.close();
	out.close();
	return 0;
}