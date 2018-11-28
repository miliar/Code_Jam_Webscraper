#include <iostream>
#include <algorithm>

int main(){
	std::cout.sync_with_stdio(false);
	
	int T, smax, res, hlp, y;
	std::cin >> T;
	std::string s;
	y = 1;
	while(T--){
		res = 0;
		std::cin >> smax >> s;
		hlp = s[0] - '0';
		for(int i=1; i<=smax; i++){
			res += std::max(0, i - hlp);
			hlp += (std::max(0, i-hlp) + s[i] - '0');
		}
		std::cout << "Case #" << y << ": " << res << "\n";
		y++;
	}
}