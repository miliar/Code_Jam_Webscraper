#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

void binary(int n, string &s) {
	int r;

	if(n <= 1) {
		s += to_string(n);
		return;
	}

	r = n%2;
	binary(n >> 1, s);    
	s += to_string(r);
}

long interp(string s, int b) {
	long adder = 1;
	long ans = 0;
	for (int j = s.length() - 1; j >= 0; --j) {
		ans += (s[j] == '1') * adder;
		adder *= b;	
	}
	//cout << adder << endl;
	return ans;
}

bool is_prime(long n, long &f) {
	for (long a = 2; a <= sqrt(n); ++a) {
		if (n % a == 0) {
			f = a;			
			return 0;		
		}	
	}
	return 1;
}

bool prime(string s, vector<int> &v) {
	for (int j = 2; j <= 10; ++j) {
		long f = -1;		
		if (is_prime(interp(s,j), f))
			return 0;
		v.push_back(f);
	}
	return 1;
}

int main() {
	//cout << interp("101", 2) << endl;
	//cout << interp("1011", 3) << endl;
	//cout << interp("1010", 4) << endl;
	cout << "Case #1\n";
	int N = 16, J = 50;
	int lol = 1;
	for (int j = (1<<N-1); j < (1<<N) && J; ++j) {
		string s = "";		
		binary(j, s);
		if (s[0] != '0' && s[N-1] != '0')
		{
			vector<int> v;
			if (prime(s, v) && J > 0) {
				//cout << "Case #" << lol << ": ";
				++lol;			
				--J;
				cout << s;
				for (int i = 0; i < 9; ++i) {
					cout << " " << v[i];
				}
				cout << endl;		
			}		
		}	
	}
}

//1000000000000000
