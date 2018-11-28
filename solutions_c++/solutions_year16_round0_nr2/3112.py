#include <cmath>
#include <iostream>
#include <queue>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <vector>

#define RETURN_TYPE unsigned

std::string flip(const std::string& S, unsigned n) {
	unsigned size = S.size();
	if (n > size) n = size;
	std::string result(size, '_');
	for (unsigned i = 0; i < n; i++) {
		result[n - 1 - i] = (S[i] == '+') ? '-' : '+';
	}
	for (unsigned i = n; i < size; i++) {
		result[i] = S[i];
	}
	return result;
}

void round(unsigned& counter, std::string& S) {
	int size = S.size();
	int i;
	for (i = size - 1; i >= 0; i--) {
		if (S[i] == '-') {
			break;
		}
	}
	if (i == -1) {
		return;
	}
	int offset = i + 1;
	for (i = 0; i < size; i++) {
		if (S[i] == '-') {
			break;
		}
	}
	if (i == 0) {
		S = flip(S, offset);
	} else {
		S = flip(S, i);
	}
	counter++;
	round(counter, S);
}

RETURN_TYPE parse(std::string S){
	unsigned counter = 0;
	round(counter, S);
	return counter;
}

int main(){
	int numberOfCases, i = 0;
	std::string S;
	
	std::cin >> numberOfCases;
	for (int i = 0; i < numberOfCases; i++) {
		std::cin >> S;
		RETURN_TYPE r = parse(S);
		std::cout << "Case #" << (i+1) << ": " << r;
		if (i != numberOfCases - 1) {
			std::cout << std::endl;	
		}
	}
}