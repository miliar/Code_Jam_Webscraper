#include <iostream>
#include <cmath>
#include <sstream>

int T;
long long  A, B;

int main(){
	std::cin >> T;
	for(int i=0; i<T; ++i){
		std::cin >> A >> B;
		long long Ac = sqrt(A);
		long long  Bc = sqrt(B);
		std::ostringstream ist;
		ist << Ac;
		std::string As = ist.str();
		ist.str(""); ist.clear();
		ist << Bc;
		std::string Bs = ist.str();
		int cA = std::ceil(As.size()/2.0);
		int cB = std::ceil(Bs.size()/2.0);
		std::istringstream ost(As.substr(0, cA));
		int Af, Bf;
		ost >> Af;
		std::istringstream ost2(Bs.substr(0, cB));
		ost >> Bf;
		std::cout << Af << " " << Bf << std::endl;
		while(As != Bs){
			std::string rev1(As.rbegin(), As.rend());
			std::string palin1 = As+rev1;
			std::string palin2 = As+rev1.substr(1);
			std::cout << palin1 << " " << palin2 << std::endl;
			break;
		}
		std::cout << As.substr(0, cA) << " " << Bs.substr(0, cB) << std::endl;
	}
}