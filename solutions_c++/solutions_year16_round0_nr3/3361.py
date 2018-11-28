#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <algorithm>
#include<cmath>

using namespace std;

static void permute(const std::string &base, int count, ofstream& fs) {
    if (!count) {
			fs <<"1" << base << "1" << '\n';
    } else {
        for (char l = '0'; l <= '1'; ++l) {
					permute(base + l, count - 1, fs);
        }
    }
}

long long isNotPrime(long long num){
	for (long long i=2; i<=sqrt(num); i++){
		if (num % i == 0) return i;
	}
	return 0;
}


int main() {
	int round_num, n, j;
	ifstream fs, get_str;
	ofstream perm_fs;
  fs.open ("input.txt");
	fs >> round_num >> n >> j;
	fs.close();

	cout << "Case #" << 1 << ":" << endl;

	perm_fs.open("inter.txt");
	permute("", n-2, perm_fs);
	perm_fs.close();

	get_str.open("inter.txt");
	int count=0;
	while (count < j){
		string str;
		getline(get_str, str);
		vector<long long> factors;
		bool valid = 0;

		for (int base = 2; base < 11; base++){
			long long interp = 0, exp = 1;
			for (int i=n-1; i>=0; i--){
				interp += (str[i] - '0')*exp;
				exp *= base;
			}
			//cout<<interp << " " << isNotPrime(interp)<<base<<endl;
			if (!isNotPrime(interp)) break;
			if (base==10) valid = 1;

			factors.push_back(isNotPrime(interp));
		}

		if (valid) {
			cout << str;
			for (int i=0; i<factors.size(); i++)
				cout << " " << factors[i];
			cout<<endl;

			count++;
		}
	}

	return 0;
}
