#include <iostream>

int main(){
	int cases;
	std::cin >> cases;

	for(int i=0; i<cases; i++){
		int b;
		long long int m;
		std::cin >> b >> m;
		if(m>(1<<(b-2))){
			std::cout << "Case #" << i+1 << ": IMPOSSIBLE" <<std::endl;
			continue;
		}
		std::cout << "Case #" << i+1 << ": POSSIBLE" << std::endl;
		std::cout << 0;
		long long int t = 1<<(b-3);
		for(int j=1; j<(b-1); j++){
			if(m>=t){
				std::cout << 1;
				m-=t;
			}else{
				std::cout << 0;
			}
			t=t>>1;
		}
		if(m==1){
			std::cout << 1;
		}else{
			std::cout << 0;
		}
		std::cout << std::endl;

		for(int j=1; j<b; j++){
			for(int k=0; k<b; k++){
				if(j<k){
					std::cout << 1;
				}else{
					std::cout << 0;
				}
			}
			std::cout << std::endl;
		}
	}
	return 0;
}


