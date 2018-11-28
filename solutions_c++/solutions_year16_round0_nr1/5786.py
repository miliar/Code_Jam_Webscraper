#include <iostream>

short check = 0xffff;
short mask[10] =
{
	0x0001,
	0x0002,
	0x0004,
	0x0008,
	0x0010,
	0x0020,
	0x0040,
	0x0080,
	0x0100,
	0x0200,
};

void clear() {
	check = 0xffff;
}

bool done(short digit) {
	check = check & (~mask[digit]);

	return !(~(check ^ 0x03FF));
}

int solve(unsigned long long N) {
	clear();

	if (N == 0) {
		return 0;
	}

	unsigned multiply = 1;
	while(true) {
		unsigned long long tempInput = N*multiply;	
		
		while(tempInput > 0) {
			short digit = tempInput%10;
			tempInput = tempInput/10;

			if (done(digit)){
				return N*multiply;
			}
		}

		multiply++;
	}
}


int main() {
	unsigned cases;

	std::cin >> cases;

	for(unsigned i=0; i<cases; ++i) {
		unsigned long long N;
		std::cin >> N;

		int solution = solve(N);

		std::cout << "Case #" << i+1 << ": ";
		if (solution == 0) {
			std::cout << "INSOMNIA" << std::endl;
		}
		else {
			std::cout << solution << std::endl;
		}
	}



}