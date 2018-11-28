#include <iostream>
#include <string>

int main(){
	int T;
	std::cin >> T;
	for(int t=1; t<=T; ++t){
		std::cout << "Case #" << t << ": ";
		std::string s;
		std::cin >> s;
		int r=0;
		char p='+';
		for(auto c=rbegin(s); c!=rend(s); ++c){
			if(*c!=p)
				++r;
			p=*c;
		}
		std::cout << r << "\n";
	}
}
