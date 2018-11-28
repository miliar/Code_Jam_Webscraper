#include <iostream>
#include <vector>

int main() {
	int T;
	int K;
	int C;
	int S;
	std::cin >> T;
	for (int i = 1; i <= T; i++) 
	{
		std::cin >> K >> C >> S;
		std::cout << "Case #" << i << ":";
		for (int j = 1; j <= K; j++)
			std::cout << " " << j;
		std::cout << endl; 
	}

}

