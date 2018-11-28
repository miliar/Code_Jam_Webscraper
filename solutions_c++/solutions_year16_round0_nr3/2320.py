#include <algorithm>
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

vector<int> primes;

int nextTest = 3;

bool isPrime(int m) {
	int tmp = int(sqrt(m));
	for (auto p : primes) {
		if (p > tmp)
			break;
		if (m % p == 0)
			return false;
	}
	return true;
}

void getPrime(int m) {
	while (nextTest <= m) {
		if (isPrime(nextTest))
			primes.push_back(nextTest);
		++nextTest;
	}
}

int getDivisor(long long s) {
	int tmp = int(sqrt(s));
	getPrime(tmp);
	for (auto p : primes) {
		if (p > tmp)
			break;
		if (s % p == 0) {
			return p;
		}
	}
	return 0;
}

long long getNum(int w, int m, int base) {
	long long s = 1;
	long long p = 1;
	for (int i = 0; i < w - 2; ++i) {
		p *= base;
		if ((m & (1 << i)) > 0)
			s += p;
	}
	p *= base;
	s += p;
	return s;
}

char * i2b(int m, int w) {
	char * str = new char[w + 1];
	int cnt = 0;
	while (m > 0) {
		if (m & 1 != 0)
			str[cnt++] = '1';
		else
			str[cnt++] = '0';
		m >>= 1;
	}
	while (cnt < w)
		str[cnt++] = '0';
	reverse(str, str + w);
	str[w] = 0;
	return str;
}

void work(ifstream & fin, ofstream & fout, int caseno) {
	int n, j;
	fin >> n >> j;
	fout << "Case #1:" << endl;
	vector<int> ds;
	int cnt = 0;
	for (int i = 0; i < (1 << (n - 2)); ++i) {
		bool isJamCoin = true;
		ds.clear();
		for (int j = 10; j >= 2; --j) {
			long long s = getNum(n, i, j);
			int divisor = getDivisor(s);
			if (divisor == 0) {
				isJamCoin = false;
				break;
			}
			ds.push_back(divisor);
		}
		if (isJamCoin) {
			fout << "1" << i2b(i, n - 2) << "1";
			reverse(ds.begin(), ds.end());
			for (auto d : ds)
				fout << " " << d;
			fout << endl;
			// debug
			/*for (int j = 2; j <= 10; ++j)
				fout << getNum(n, i, j) << " ";
			fout << endl;*/
			if (++cnt == j)
				break;
		}
	}
}

int main() {
	ifstream fin;
	fin.open("input");
	ofstream fout;
	fout.open("output");
	int testcase;
	fin >> testcase;
	primes.push_back(2);
	for (int i = 0; i < testcase; ++i) {
		work(fin, fout, i + 1);
	}
	fin.close();
	fout.close();
	return 0;
}