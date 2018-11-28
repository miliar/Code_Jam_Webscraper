#include <iostream>

int T;
int N, M;
int map[101][101];

int main(){
	std::cin >> T;
	for(int p=0; p<T; ++p){
		std::cin >> N >> M;
		for(int i=0; i<N; ++i){
			for(int j=0; j<M; ++j){
				std::cin >> map[i][j];
			}
		}
		bool b = true;
		for(int i=0; i<N; ++i){
			for(int j=0; j<M; ++j){
				int cur = map[i][j];
				bool chk1 = true, chk2 = true;
				//std::cout << "-> " << i << " " << j << std::endl;
				for(int k=0; k<M; ++k){
					//std::cout << i << " " << k << std::endl;
					if(map[i][k] > cur) {
						chk1 = false;
						break;
					}
				}
				for(int k=0; k<N; ++k){
					if(map[k][j] > cur) {
						chk2 = false;
						break;
					}
				}
				if(chk1==false && chk2 == false){
					b = false;
					break;
				}
			}
			if(!b) break;
		}
		
		if(b) std::cout << "Case #" << (p+1) << ": " << "YES" << std::endl;
		else std::cout << "Case #" << (p+1) << ": " << "NO" << std::endl;
	}
}