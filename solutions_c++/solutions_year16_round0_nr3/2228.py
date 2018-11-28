#include <bitset>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <sstream>
#include <vector>

using namespace std;

bool is_prime(long num, long &divisor) {
	for (long i = 2; i * i <= num; ++i) {
		if (num % i == 0) {
			divisor = i;
			return false;
		}
	}
	return true;
}

string to_binary(long num) {
	long m = num; 
	string ret = ""; 
	while (num) {
		if (num % 2) {
			ret = "1" + ret;
		} else {
			ret = "0" + ret;
		}
		num /= 2;
	}
	return ret; 
}

long to_base(long num, long b) {
	long m = num;
	long sum = 0;
	long cur = 1;
	while (num) {
		if (num % 2) {
			sum += cur;
		}
		cur *= b;
		num /= 2;
	}
	string bin = to_binary(m);
	return sum; 
}

bool is_jamcoin(long num, long len, vector<long> &proof) {
	for (long i = 0; i < 9; ++i) {
		long b = i+2;
		long inNewBase = to_base(num, b);
		if (is_prime(inNewBase, proof[i])) {
			return false;
		}
	}
	return true;
}

void solve_case(long N, long J, long case_num) {
  	stringstream answer;
  	answer << endl;

  	vector<long> proof(9);
  	for (long i = 2; i <= 10; ++i) {
  		proof[i-2] = 1;
  		for (int j = 0; j < N/2; ++j) {
  			proof[i-2] *= i;
  		}
  		proof[i-2] += 1;
  	}

  	long base = (1<<(N/2-1))+1;
  	while (J) {
  		long num = (base << (N/2)) + base;
  		answer << to_binary(num);
  		for (int i = 0; i < 9; ++i) {
  			answer << " ";
  			answer << proof[i];
  		}
  		answer << endl;
  		J--; 
  		base += 2;
  	}

  	cout << "Case #" << case_num+1 << ": " << answer.str() << "\n";
}


int main() {
  	int T;
  	cin >> T;
  	for (int i = 0; i < T; i++) {
		int N, J;
		cin >> N >> J;
   	 	solve_case(N, J, i);
  	}
}
