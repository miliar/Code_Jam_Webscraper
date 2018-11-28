#include <iostream>
#include <fstream>
#include <set>

void add_digits(std::set<long> *a, long n) {
	long tmp = n;
	while (tmp != 0) {
		a->insert(tmp % 10);
		tmp = tmp / 10;
	}
}

long getVal(long n) {
	if (n==0) return 0;
	
	std::set<long> a;
	long acc = 0;
	while (a.size() < 10 || acc < 0) {
		acc += n;
		add_digits(&a,acc);
	}
	return (acc > 0) ? acc :0;
}

int main(int argc, char **argv) {
	int t;
	std::ifstream input;
	std::ofstream output;
	
	input.open("A-large.in");
	output.open("out.txt");
	input >> t;
	for (int i = 1;i<=t;i++) {
		long n;
		input >> n;
		
		long val = getVal(n);
		output << "Case #" << i << ": ";
		if (val == 0) output << "INSOMNIA";
		else output << val;
		output << std::endl;
	
	}
    input.close();
	output.close();
	return 0;
}
