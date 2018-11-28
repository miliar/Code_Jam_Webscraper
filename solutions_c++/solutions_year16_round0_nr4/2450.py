#include <cmath>
#include <iostream>
#include <queue>
#include <sstream>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <vector>

std::string parse(unsigned long long K, unsigned long long C, unsigned long long S){
	std::stringstream ss;
	for (unsigned i = 0; i < S; i++) {
		//ss << (i * pow(K, C - 1) + 1);
		ss << (i + 1);
		if (i != S - 1) {
			ss << " ";
		}
	}
	return ss.str();
}

int main(){
	int T, i = 0;
	unsigned long long K, C, S;
	
	std::cin >> T;
	for (int i = 0; i < T; i++) {
		std::cin >> K >> C >> S;
		auto r = parse(K, C, S);
		std::cout << "Case #" << (i+1) << ": " << r << std::endl;
	}
}