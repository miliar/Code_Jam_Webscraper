#include <iostream>
#include <algorithm>

int main(){
	std::cout.sync_with_stdio(false);
	
	int T, X, R, C, y;
	std::cin >> T;
	y = 1;
	while(T--){
		std::cin >> X >> R >> C;
		if(X >= 7 || X >= (2*std::min(R, C) + (R!=C)) || (R*C)%X || (X==4 && std::min(R,C) == 2) || (X==6 && R*C == 12)) std::cout << "Case #" << y << ": " << "RICHARD\n";
		else std::cout << "Case #" << y << ": " << "GABRIEL\n";
		y++;
		}
	}