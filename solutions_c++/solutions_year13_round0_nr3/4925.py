#include <iostream>
#include <string>
#include <algorithm>
#include <functional>
#include <list>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <cstdio>
#include <cstring>
#include <cmath>

bool isPalindromes(unsigned long long int n) {
	char* str = new char[0xFF];
	sprintf(str, "%u", n);
	unsigned int len = strlen(str) - 1;
	for(unsigned int l=0; l<=len/2; ++l) {
		if(str[0+l] != str[len-l]) return false;
	}
	delete str;
	
	return true;
}

unsigned long long int solve(unsigned long long int A, unsigned	long long int B) {
	unsigned long long int begin = static_cast<unsigned long long int>( floor(sqrt(A)) );
	unsigned long long int end   = static_cast<unsigned long long int>(  ceil(sqrt(B)) );
	unsigned long long int count = 0;
	for(unsigned long long int n=begin; n<=end; ++n) {
		if(isPalindromes(n) && isPalindromes(n*n)) {
			if((A <= n*n) && (n*n <= B)) ++count;
		}
	}
	
	return count;
}

int main(int argc, char** argv) {
	unsigned int T;
	std::cin >> T;
	
	for(unsigned int t=0; t<T; ++t) {
		unsigned long long int A, B;
		std::cin >> A >> B;
		
		std::cout << "Case #" << (t+1) << ": " << solve(A, B) << std::endl;
	}
	
	return 0;
}
