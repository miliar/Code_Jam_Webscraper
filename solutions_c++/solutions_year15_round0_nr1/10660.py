#include <iostream>
#include <sstream>

int main(int argc, const char * argv[]) {
	int T = 0;
	std::cin >> T;
	
	std::string line;
	std::getline(std::cin, line);
	for(int t=1; t<=T; t++){
		std::getline(std::cin, line);
		std::stringstream stream(line);
		
		std::string smax;
		stream >> smax;
		
		std::string audience;
		stream >> audience;
		
		int ans = 0, sum = 0;
		for(int x=0; x<audience.size(); x++){
			int a = audience[x] - '0';
			if(a > 0 && sum < x){
				ans += x - sum;
				sum = x;
			}
			sum += a;
		}
		std::cout << "Case #" << t << ": " << ans << std::endl;
	}
}
