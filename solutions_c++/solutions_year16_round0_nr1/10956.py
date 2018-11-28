#include <iostream>
typedef unsigned long long int uint;
const uint END = 2046;
int main(int argc, char const *argv[]){
	uint T,N;
	std::cin >> T;
	for(uint i = 1; i <= T; i++){
		std::cin >> N;
		uint n = 0, b = 0;
		while((b != END) && (n + N > n)){
			n += N;
			for(uint m = n; m > 0; m /= 10){
				uint d = m % 10;
				b |= 1 << (d + 1);
			}
		}
		std::cout << "Case #" << i << ": ";
		if(b == END){
			std::cout << n << std::endl;
		}else{
			std::cout << "INSOMNIA" << std::endl;
		}
	}
	return 0;
}