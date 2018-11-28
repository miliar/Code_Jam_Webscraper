#include <iostream>

unsigned number_to_mask(unsigned n){
	unsigned d=0;
	do{
		d |= 1<<(n%10);
	} while(n /= 10);
	return d;
}

int main(){
	int T;
	std::cin >> T;
	for(int t=1; t<=T; ++t){
		unsigned n;
		std::cin >> n;
		std::cout << "Case #" << t << ": ";

		unsigned d=0;
		for(unsigned m=1; m<1000; ++m){
			d |= number_to_mask(n*m);
			if(d==1023){
				std::cout << (m*n);
				goto endt;
			}
		}
		std::cout << "INSOMNIA";
endt:
		std::cout << '\n';
	}
}
