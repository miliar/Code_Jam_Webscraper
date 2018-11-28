#include <iostream>
#include <vector>
using namespace std;

int main() {
	int T, K, C, S;
	std::cin >> T;
	int res = 0;
	for (int i = 1; i <= T; i++) 
	{
		std::cin >> K >> C >> S;
		cout << "Case #" << i << ":";
		for (int j = 1; j <= K; j++)
			cout << " " << j;
		cout << endl; 
	}

}

