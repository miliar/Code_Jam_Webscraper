#include <iostream>
#include <string>
#include <bitset>
#include <vector>
#include <sstream>
#include <math.h>
#include <stdint.h>
using namespace std;

void print(vector<uint64_t> v) {
	cout << "|";
	for(int i = 0; i < v.size(); i++) {
		cout << v[i] << " ";
	}
	cout << endl;
}	

vector<uint64_t> factors(const vector<uint64_t> &v) {
	vector<uint64_t> factors;
	for(int i = 0; i < v.size(); i++) {
		for(int k = 2; k < sqrt(v[i])+1; k++) {
			if(v[i]%k==0) {
				factors.push_back(k);
				break;
			}
		}
	}
	return factors;
}

uint64_t s_to_i(const string &s) {
	istringstream ss(s);
	uint64_t i;
	ss >> i;
	return i;
}

vector<uint64_t> get_base_n(string b_set) {
	uint64_t num = s_to_i(b_set);
	
	vector<uint64_t> bases;
	for(int i = 2; i <= 10; i++) {
		uint64_t tmp = num;
		uint64_t res = 0, rem = 0, k = 0;
		while(tmp != 0) {
			rem = tmp % 10;
			tmp /= 10;
			res += rem * pow(i,k);
			k++;
		}
		bases.push_back(res);
	}
	return bases;
}

int main(int argc, char *argv[]) {
	int t;
	cin >> t;
	int n,j;
	cin >> n >> j;
	
	uint64_t range = pow(2,n)-1;
	uint64_t start = 1 + pow(2,n-1);
	cout << "Case #1:" << endl;
	for(int i = start; i < range; i++) {
		bitset<16> foo(i);
		string s = foo.to_string();
		size_t idx = s.find_first_of("1");
		string fixed = s.substr(idx,s.length());
		if(fixed[0] == '0' || fixed[fixed.length()-1] == '0') {
			continue;
		}
		vector<uint64_t> v = get_base_n(fixed);
		vector<uint64_t> f = factors(v);

		if(f.size() == 9 && j-->0) {
			cout << fixed;
			for(int i = 0; i < f.size(); i++) {
				cout << " " << f[i];
			}
			cout << endl;
		}
		if(j == 0) {
			break;
		}
	}

	return 0;
}
