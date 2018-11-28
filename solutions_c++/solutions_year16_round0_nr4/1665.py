#include <iostream>
#include <cmath>
#include <vector>


int main()
{
	int cases;
	std::cin >> cases;
	for (int i = 1; i <= cases; i++) {
		int K, C, S;
		std::cin >> K >> C >> S;
		int ceil = (int)std::ceil((float)K / C);
		std::cout << "Case #" << i << ":";
		if (ceil > S) {
			std::cout << " IMPOSSIBLE";
		}
		else if (C == 1 && K == 1){
			std::cout << " 1";
		}
		else {			
			for (int j = 1; j <= K; j++) {
				std::cout << " " << j;
			}
		}
		std::cout << std::endl;
	}

    return 0;
}

