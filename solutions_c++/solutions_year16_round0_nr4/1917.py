#include <iostream>

int main(){
	int T;
	std::cin >> T;
	for(int t=1; t<=T; ++t){
		int K, C, S;
		std::cin >> K >> C >> S;
		std::cout << "Case #" << t << ":";
		for(int i=1; i<=K; ++i)
			std::cout << " " << i;
		std::cout << "\n";
	}
}
