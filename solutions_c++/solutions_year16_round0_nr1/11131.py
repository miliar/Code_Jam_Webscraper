#include <iostream>
#include <cstdint>

using namespace std;

int digit[10];
int num_digits_found;

void solve(uint32_t N)
{
	if (N == 0) {
		cout << "INSOMNIA";
		return;
	}
	for (int i = 0; i < 10; ++i) {
		digit[i] = 0;
	}
	num_digits_found = 0;
	int i = 1;
	while (1) {
		uint64_t num = N * i;
		uint64_t temp = num;
		while (num != 0) {
			int current_digit = num % 10;
			num = num / 10;
			if (digit[current_digit] == 0) {
				digit[current_digit] = 1;
				num_digits_found++;
				if (num_digits_found == 10) {
					cout << temp;
					return;
				}
			}
		}
		++i;
	}
		
}

int main()
{
	uint32_t T, N;
	cin >> T;
	for (int i = 0; i < T; ++i) {
		cin >> N;
		cout << "Case #" << i + 1 << ": ";
		solve(N);
		cout << endl;
	}
	return 0;
}
