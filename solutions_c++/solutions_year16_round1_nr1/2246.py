#include <iostream>
#include <utility>
#include <cmath>
#include <vector>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <time.h>
#include <algorithm>
#include <string>

//using namespace std;

int cmp (int a, int b) {
	return a<b;
}

int loop() {
}

int main() {
	int T;
	std::string N;
	int count = 0;
	
	std::string result;
	
	std::cin >> T;
	
	for(int i = 0; i < T; i++) {
		result = "";
		std::cin >> N;
		//std::cout << N << std::endl;
		count = 0;
		for(std::string::iterator it = N.begin(); it != N.end(); ++it) {
			//std::cout << N[count] << std::endl;
			//std::cout << N.front();
			if(count == 0) {
			
				//result.insert(N[count]);
				result = N[count];
			} else if(N[count] < result[0]) {
				result = result + N[count];
				//result.insert(result.front(), N[count]);
				 //strcat(N[count], result);
			} else {
			result = N[count] + result; 
							//result.insert(result.back(), N[count]);
				 //strcat(result, N[count]);			
			}
			//puts(result);
			
			count++;
		}
		std::cout << "Case #" << i+1 << ": " << result << std::endl;
	}
	return 1;
}