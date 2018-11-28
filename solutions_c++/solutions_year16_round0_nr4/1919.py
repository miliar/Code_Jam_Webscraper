#include <iostream>
#include <string>
#include <vector>
#include <math.h>
#include <sstream>
#include <iomanip>

std::string getTile(int MaxTiles, int tile)
{
	std::ostringstream oss;
	MaxTiles = MaxTiles >> 1;
	while (MaxTiles > 0) {
		oss << (const char*) (((tile&MaxTiles) == MaxTiles) ? "G" : "L");
		MaxTiles = MaxTiles >> 1;
	}
	return oss.str();
}
void printFractiles(int K, int C)
{
	std::cout << std::endl;
	const int MaxTiles = 1 << K;
	for (int i = 0; i < MaxTiles; i++) {
		const std::string tile(getTile(MaxTiles, i));
		const std::string gtile(K,'G');
		std::string result = tile;
		for (int j = 0; j < C - 1; j++) {
			for (int k = 0; k < result.length(); k=k+K) {
				if (result[k] == 'L') {
					result.replace(k, 1, tile);
				} else {
					result.replace(k, 1, gtile);
				}
			}
		}
		std::cout << result << std::endl;
	}
}

// Simple Case Algorithm 
// K = 3 (LLL, LLG, LGL, LGG, GLL, GLG, GGL, GGG) <= 2^3 = 8 starting tiles
// C = 2 .. 8 configurations with 3^2 tiles total
// M = K^C = Total tiles K=3, C=1 M=3, C=2 M=9, C=3 M=27 ...
// Solution = K^(C-1)*(0,1,2,3..K) + 1
// E.g. K=3, C=2, S=3 
// Sol => M=9, Sol = 1, 4, 7
// K=4, C=2, S=4
// Sol => M=16, Sol = 1, 5, 9, 13
void getSimplePos(int K, int C)
{
#pragma float_control(precise, on, push)
	//printFractiles(K, C);
	unsigned long long N = ::pow((unsigned long long)K, (unsigned long long)C - 1);
	//unsigned int N = ::pow((double) K, (double) C - 1);
	for (int i = 0; i < K; i++) {
		std::cout << std::fixed << (N*i +1) << " ";
#pragma float_control(pop)
	}
}
void getComplexPos(int K, int C, int S)
{
	std::cout << "IMPOSSIBLE";
}

int main()
{
	int NumTests = 0;
	std::cin >> NumTests; // only 1
	for (int i = 1; i <= NumTests; i++) {
		int K = 0, C = 0, S = 0;
		std::cin >> K >> C >> S;
		if (K == S) {
			std::cout << "Case #" << i << ": "; getSimplePos(K, C); 
		} else {
			std::cout << "Case #" << i << ": "; getComplexPos(K, C, S); 
		}
		std::cout << std::endl;
	}
	return 0;
}
