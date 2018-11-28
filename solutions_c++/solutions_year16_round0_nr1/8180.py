// counting sheep

#include <fstream>
#include <cstdlib>

bool andAll(bool arr[], int size) {
	bool ret = true;

	for (int i = 0; i < size; ++i) {
		ret &= arr[i];
	}

	return ret;
}

void setDigits(bool digits[], int n) {
	while (n > 0) {
		div_t divresult = div(n, 10);

		digits[divresult.rem] = true;
		n = divresult.quot;
	}
}

int solve(int multiplier) {
	bool digitChecks[10];
	int n;

	memset(digitChecks, false, 10);

	for (int i = 1; !andAll(digitChecks, 10); ++i) {
		n = i * multiplier;
		setDigits(digitChecks, n);
	}

	return n;
}

int main(int argc, char **argv) {
	std::ifstream input;
	std::ofstream output;

	input.open("A-large.in");
	output.open("output.txt");

	int t;

	input >> t;

	for (int iT = 1; iT <= t; ++iT) {
		int n;

		input >> n;

		if (n == 0) {
			output << "Case #" << iT << ": INSOMNIA" << std::endl;
		} else {
			int answer = solve(n);
			output << "Case #" << iT << ": " << answer << std::endl;
		}
	}

	input.close();
}
