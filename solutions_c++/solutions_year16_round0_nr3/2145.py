#include <iostream>
#include <fstream>

//Uses the fact that a1 * q^{2n-1} + b1 * q^{2n-2} + a2 * q^{2n-3} + ... +
//+ a{n-1} * q^3 + b{n-1} * q^2 + an * q * bn divisible by (q+1) if
// sum(a{i}) = sum(b{i})
//works only, if digits is even, and order < 2^{(digits-2)/2}, which is true
//with 50 < 2^7 and 500 < 2^15
void produce_nth_jamcoin(std::ofstream *output, int digits, int order) {
	(*output) << 1;
	for (int i = 0; i< digits-2; i+=2) {
		int tmp = (order & 1);
		(*output) << tmp << tmp;
		order = order >> 1;
	} 
	(*output) << 1;
	(*output) << " 3 4 5 6 7 8 9 10 11" << std::endl;
}

int main(int argc, char **argv) {
	int t;
	std::ifstream input;
	std::ofstream output;
	
	input.open("C-large.in");
	output.open("out.txt");
	input >> t;
	for (int i = 1;i<=t;i++) {
		int n;
		int j;
		input >> n;
		input >> j;
		
		output << "Case #" << t << ":" << std::endl;
		for (int k = 0; k < j; k++) produce_nth_jamcoin(&output,n,k);
	
	}
    input.close();
	output.close();
	return 0;
}
