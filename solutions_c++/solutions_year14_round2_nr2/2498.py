#include <vector>
#include <iostream>

int main(){
	int n;
	std::cin >> n;
	const int N = n;
	while(n--){
		int A,B,K;
		std::cin >> A >> B >> K;
		int wins = 0;
		for(int i = 0; i < A; i++){
			for(int j = 0; j < B; j++){
				if( (i & j) < K){
					wins++;
				}
			}
		}
		std::cout << "Case #" << (N -n) << ": " << wins << std::endl;
	}
	return 0;
}
