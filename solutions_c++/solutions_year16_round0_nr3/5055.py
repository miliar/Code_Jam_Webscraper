#include <iostream>
#include <stdlib.h>
#include <string>
#include <vector>
#include <map>
#include <cmath>
#include <fstream>
using namespace std;

long long int toNum(string str, int base)
{
	long long int num = 1;
	for (int i=1; i<str.size(); i++)
	{
		num = num*base + (str[i]-'0');
	}
	return num;
}

string generateStr(int n)
{
	string s = "1";
	for (int i=0; i < n-2; ++i) {
		if (rand()%2 == 0) {
			s += "0";
		} else {
			s += "1";
		}
	}
	s += "1";
	return s;
}

long long int isComposite(long long int num)
{
	for (long long int i=2; i<= 500; ++i) {
		if (num%i == 0) {
			return i;
		}
	}
	return 0;
}

void solve(int n, int j)
{
	ofstream outfile("out.txt");
		outfile << "Case #1:" << endl;
	map<string, bool> m;
	int numFound = 0;
	while (numFound < j) {
		vector<int> factors;
		string s = generateStr(n);
		if (m.find(s) != m.end()) {
			continue;
		}
		m[s] = true;
		int factor = 0;
		long long int num;
		for (int base=2; base <= 10; ++base) {
			num = toNum(s, base);
			factor = isComposite(num);
			if (!factor) {
				break;
			}
			factors.push_back(factor);
		}
		if (!factor) {
			continue;
		}
		outfile << s; //<< " " << num;
		for (int k=0; k< factors.size(); ++k) {
			outfile << " " << factors[k];
		}
		outfile << endl;
		++numFound;
	}
	outfile.close();
}

int main()
{
	solve(16, 50);
}
