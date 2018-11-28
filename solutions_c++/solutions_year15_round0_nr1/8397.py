#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

int main() {
	int t;
	
	std::cin >> t;
	for(int i = 0; i < t; ++i) {
		std::string s;
		int smax;
		
		std::cin >> smax >> s;
		
		int res = 0;
		int cum = 0;
		
		for(int j = 0; j <= smax; ++j) {
			if(j > cum) {
				int dt = j - cum;
				res += dt;
				cum += dt;
			}
			
			int count = (int) (s[j] - '0');
			cum += count;
			
			//std::cerr << "cum = " << cum << std::endl;
		}
		
		//std::cerr << "=================" << std::endl;
		
		std::cout << "Case #" << (i+1) << ": " << res << std::endl;
	}
	
	return 0;
}
