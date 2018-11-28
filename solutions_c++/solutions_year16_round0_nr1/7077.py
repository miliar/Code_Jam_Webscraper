#include <iostream>
#include <string>

int main() {
	int T, t, N, n;
	
	std::cin >> T;
	for (t=0; t<T; t++) {
		bool counted[10] = {false, false, false, false, false, false, false, false, false, false};
		bool awake = true;
		std::cin >> N;
		int num = N;
		for (n=1; awake && num!=0; n++) {
			num = N*n;
			//std::cout << "Current Number: " << num << std::endl;
			
			int D = num;
			while (D!=0) {
				counted[D%10] = true;
				//std::cout << "\tFound: " << D%10 << std::endl;
				D/=10;
			}
			
			int c;
			int p = 0;
			//std::cout << "[";
			for (c=0; c < 10; c++) {
				//std::cout << c << "(";
				if (counted[c]) {
					p++;
					//std::cout << "+)";
				} else {
					//std::cout << "-)";
				}
				//std::cout << ",";
			}
			//std::cout << "]" << std::endl;
			if (p==10) awake = false;
		}
		std::cout << "Case #" << t+1 << ": ";
		if (awake == false)
			std::cout << num;
		else 
			std::cout << "INSOMNIA";
		std::cout << std::endl;
	}
}
