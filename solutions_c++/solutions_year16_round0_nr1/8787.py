#include <iostream>
#include <vector>

int main(){
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(nullptr);
	std::cout.tie(nullptr);
	unsigned t;
	std::cin >> t;
	for(unsigned i = 0; i < t; ++i){
		unsigned long long n;
		std::cin >> n;
		if(n == 0){
			std::cout << "Case #" << i + 1 << ": INSOMNIA\n";
			continue;
		}
		std::vector<bool> occ(10, false);
		unsigned cnt = 0;
		for(unsigned j = 1; true; ++j){
			unsigned long long val = n * j;
			while(val != 0){
				unsigned digit = val % 10;
				if(occ[digit] == false){
					occ[digit] = true;
					++cnt;
				}
				val /= 10;
			}
			if(cnt == 10){
				std::cout << "Case #" << i + 1 << ": " << n * j << "\n";
				break;
			}
		}
	}

	return 0;
}
