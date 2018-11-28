#include <iostream>
#include <vector>
#include <iomanip>
#include <string>

using std::cin;
using std::string;
using std::vector;

void solveCase() {
	int A, B, K;
	cin >> A >> B >> K;
	int result = 0;
	for (int i = 0; i < A; ++i)
	{
		for (int j = 0; j < B; ++j)
		{
			result += (i & j) < K ? 1 : 0;
		}
	}
	std::cout << result;
}
int main() {
	freopen("B-small.in", "r", stdin);
	freopen("B-small.out", "w", stdout);
	int T;
	std::cin >> T;
	for (int i = 1; i < T + 1; ++i)
	{
		std::cout << "Case #" << i << ": ";
		solveCase();
		if (i < T)
			std::cout << std::endl;
	}
	return 0;
}