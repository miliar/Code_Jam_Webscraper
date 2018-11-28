#include <fstream>
#include <string>

using namespace std;

const unsigned ALL_DIGITS = 1023;

int digit_mask(unsigned n){
	int mask = 0;
	while(true){
		mask |= 1 << (n % 10);
		if (n < 10) break;
		n /= 10;
	}
	return mask;
}

int main(){
	ifstream in("A-large.in");
	ofstream out("out.txt");
	unsigned cases(0), n(0), mask(0), i(1);
	in >> cases;
	for(int c = 1; c <= cases; ++c){
		in >> n;
		if( n == 0){
			out << "Case #" << c << ": INSOMNIA\n";
		}else{
			for(i = 1, mask = 0;ALL_DIGITS & mask != ALL_DIGITS;++i){
				mask |= digit_mask(i*n);
			}
			out << "Case #" << c << ": " << (i-1)*n << "\n";
		}
	}
	out.flush();
	return 0;
}
