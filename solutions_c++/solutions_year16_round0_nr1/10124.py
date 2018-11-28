#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>

int main() {
	int N, digit, tmp, in_int;
	std::vector<int> digits, history, inputs;
	int a = 1, counter = 0;
	bool insomnia = false;

	std::fstream in("A-large.in"), out;
	out.open("output.txt");
	while (!in.eof()) {
		in >> in_int;
		inputs.push_back(in_int);
	}

	for (int k = 1; k <= inputs[0]; k++) {
		counter = 0;
		a = 1;
		N = inputs[k];
		digits.clear();
		history.clear();
		insomnia = false;
		while (true) {
			counter = 0;
			tmp = N;
			history.push_back(N);
			
			for (int i = 0; tmp > 0; i++) {
				digit = tmp % 10;
				digits.push_back(digit);
				tmp /= 10;
			}

			for (int j = 0; j < 10; j++) {
				if (std::find(digits.begin(), digits.end(), j) != digits.end()) {
					counter += 1;
				}
			}

			if (counter == 10) {
				break;
			}

			std::sort(history.begin(), history.end());
			if (std::adjacent_find(history.begin(), history.end()) != history.end()) {
				insomnia = true;
				break;
			}

			a += 1;
			N = history[0] * a;
		}
		
		out << "Case #" << k << ": ";
		if (insomnia) {
			out << "INSOMNIA\n";
		}
		else {
			out << N << "\n";
		}
	}
}