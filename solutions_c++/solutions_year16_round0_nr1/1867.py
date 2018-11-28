#include <iostream>
#include <unordered_set>
using namespace std;

void checkDigits(uint64_t num, unordered_set<int>& digitsPresent)
{
	while (num > 0) {
		int digit = num % 10;
		if (digitsPresent.find(digit) == digitsPresent.end())
			digitsPresent.insert(digit);
		num = num / 10;
	}
}

void countSheep(uint64_t N, uint i) {
	unordered_set<int> digitsPresent;
	if (N == 0) {
		cout << "Case #" << i << ": INSOMNIA" << endl;
		return;
	}
	uint64_t K = 0;
	while (digitsPresent.size() < 10) {
		K++;
		checkDigits(K*N, digitsPresent);
	}
	cout << "Case #" << i << ": " << K*N << endl;   
}

int main() {
	int T;
	uint64_t N;
	std::cin >> T;
	for (int i = 1; i <= T; i++) 
	{
		std::cin >> N;
		countSheep(N, i);

	}

}

