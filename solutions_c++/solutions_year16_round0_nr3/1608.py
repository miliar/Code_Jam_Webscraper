#include <fstream>
#include <bitset>
#include <vector>
#include <set>
using namespace std;

vector<int> primelist = { 3, 5, 7, 11, 13, 17, 19, 23 };

ofstream output;
class Prime{
private:
	void print(unsigned long number);
	ofstream output;
	vector<int> factors;
	set<unsigned long> numbers;
	int N,J;
	unsigned long block;
	int blocklen;
	unsigned long left;
	void search(unsigned long right, int pos, int len);
	int findfactor(int len, int base);
	int getfactor(int x,int base);
public:
	Prime() { 
		ifstream input;
		input.open("input.txt"); 
		int T;
		input >> T >> N >> J;
		input.close();
	}
	void generate() {
		numbers.clear();
		output.open("output.txt");
		output << "Case #1:" << endl;
		if (N == 16) {
			for (int i = 0x8001; i<=0xffff && numbers.size()<J; i += 2) {
				factors.clear();
				for (int j = 2; j <= 10; j++) {
					factors.push_back(getfactor(i,j));
					if (factors.back() < 0)
						break;
				}
				if (factors.back() > 0) {
					print(i);
				}
			}
		} else {
			for (int p = 1; p <= N; p++) {
				int n = p - 1;
				if (n * 2 > N) break;
				blocklen = n;
				block = (1 << n) - 1;
				left = block << (N - n);
				factors.clear();
				for (int i = 2; i <= 10; i++) {
					factors.push_back(findfactor(blocklen, i));
					if (factors.back() < 0) {
						break;
					}
				}
				if (factors.back() > 0) {
					search(block, n, N - 2 * n);
				}
			}
		}
		output.close();
	}



};

int main() {
	Prime p;
	p.generate();
	return 0;
}

void Prime::search(unsigned long right, int pos, int len){
	if (numbers.size() >= J) return;
	unsigned long number = left + right;
	print(number);
	for (int i = 0; i <= len - blocklen; i++) {
		search(right + (block << (pos + i)), pos + blocklen + i, len - i - blocklen);
	}
	
}
void Prime::print(unsigned long number) {
	if (numbers.find(number) != numbers.end()) {
		return;
	}
	numbers.insert(number);
	if (N < 32) {
		bitset<16> num(number);
		output << num;
	} else {
		bitset<32> num(number);
		output << num;
	}
	for (int factor : factors) {
		output << ' ' << factor;
	}
	output << endl;
}

int Prime::findfactor(int len, int base) {
	long long number = 0;
	long long fac = 1;
	for (int i = 0; i < len; i++) {
		number += fac;
		fac *= base;
	}
	for (int i = 2; i < number; i++) {
		if (number % i == 0) return i;
	}
	return -1;
}

int Prime::getfactor(int x,int base) {
	long long number = 0;
	long long fac = 1;
	while (x > 0) {
		number += fac * (x % 2);
		fac *= base;
		x /= 2;
	}
	for (int i = 2; i < sqrt(number); i++) {
		if (number % i == 0) return i;
	}
	return -1;

}

