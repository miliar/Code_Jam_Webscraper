#include<iostream>
#include<vector>
#include<string>

int count(int A, int B, int K) {
	int sum = 0;
	for (int i = 0; i < A; ++i)
		for (int j = 0; j < B; ++j)
			if ((i&j) < K)
				sum++;
	return sum;
}

int main(void) {
	int cases;
	std::cin >> cases;
	int current = 1;
	while (cases--) {
		int A, B, K;
		std::cin >> A >> B >> K;
		std::cout << "Case #" << current << ": " << count(A, B, K) << std::endl;
		current++;
	}
	return 0;
}
