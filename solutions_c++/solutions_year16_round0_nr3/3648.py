#include <iostream>  
#include <fstream>
#include <vector>
#include <string>
#include <boost/multiprecision/cpp_int.hpp>


using namespace std; 
using namespace boost::multiprecision;
cpp_int tobase(cpp_int num, cpp_int base) {
	cpp_int ret = 0;
	if (num == 1000000000000111 && base==3) {
		int z = 1;
	}
	cpp_int ten = 10;
	for (int n = 0; num > 0; n++)
	{

		ret += (num%ten)*pow(base,n);
		cpp_int str = (num%ten);
		string str2 = str.str();
		string tmp = ret.str();
		num /= ten;
		
	}
	string r = ret.str();
	return ret;
}
vector<cpp_int> primes;
cpp_int isprime(cpp_int p) {
	if (p == 32775) {
		int z = 1;
	}
	cpp_int tmp = sqrt(p);
	for (int a = 0; a < primes.size() && tmp>=primes[a]; a++) {
		if (p%primes[a] == 0) {
			return primes[a];
		}
	}
	return -1;
}
vector<vector<cpp_int>> CoinJam(unsigned int n, unsigned int j) {
	vector<vector<cpp_int>> ret;
	int sz = pow(2, 16) + 2;
	vector<bool> nums(sz);
	for (int a = 2; a < sz; a++)
		if (!nums[a]) {
			for (int b = 2; b*a < sz; b++)
				nums[b*a] = true;
		}

	
	for (int a = 2; a < sz; a++)
		if (!nums[a]) primes.push_back(a);

//	unsigned int num = 1 << n - 1;
	for (unsigned int m = 1; m < 1024*1024; m++) {
		cpp_int tmp=0;
		cpp_int pw = 10;

		unsigned int high = log2(m);
		unsigned p = high;
		if (m==446) {
			int r = 1;
		}
		for (int ptmp = high; ptmp >=0; ptmp--)
		{
			
			if (m & (1 << p)) {
				//tmp++;
				//pow(tmp, p);
				tmp+=pow(pw, p);
			}
			p--;
		}
		cpp_int c = pow(pw, n-2);
		stringstream z1;
		string z1a;
		string z2a;
		string z3a;
		string z4a;
		stringstream z2;
		stringstream z3;
		stringstream z4;
		if (m == 446) {	
			z1 << tmp;
			z1a = z1.str();
		}

		tmp += c;
		if (m == 446) {
			z2 << tmp;
			z2a = z2.str();
		}
		tmp *=10;
		if (m == 446) {
			z3 << tmp;
			z3a = z3.str();
		}
		tmp++;
		if (m == 446) {
			z4 << tmp;
			z4a = z4.str();
		}

		vector<cpp_int> curdiv;
		curdiv.push_back(tmp);
		for (cpp_int a = 2; a <= 10; a++) {
			cpp_int trans = tobase(tmp, a);
			cpp_int divtmp = isprime(trans);
			if (divtmp == -1)break;
			curdiv.push_back(divtmp);
		}
		
		if (curdiv.size() == 10)
			ret.push_back(curdiv);
		//check if it is prime in all bases
		if (ret.size() == j) break;
	}
	return ret;
}
void main() {
	ofstream outfile("2016Qual\\C-small-attempt0.out");
	vector<vector<cpp_int>> ret = CoinJam(16, 50);

	outfile << "Case #1:\n";
	for (int n = 0; n < 50; n++) {
		for (int m = 0; m < 9; m++)
			outfile << ret[n][m] << " ";
		outfile << ret[n][9] << "\n";
	}

}