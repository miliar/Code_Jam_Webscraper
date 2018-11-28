#include <iostream>
#include <string>

int main(int argc, char **argv){
	int casos;
	std::cin>>casos;
	for(int K=1; K<=casos; ++K){
		int shyness; std::cin>>shyness;
		std::string array; std::cin>>array;
		int
			invitar=0,
			total=0;

		for(int L=0; L<array.size(); ++L){
			if(array[L]-'0' == 0) continue;
			if(total<L){
				invitar += L-total;
				total=L;
			}

			total += array[L]-'0';
		}
		std::cout << "Case #" << K << ": " << invitar << '\n';
	}
	return 0;
}
