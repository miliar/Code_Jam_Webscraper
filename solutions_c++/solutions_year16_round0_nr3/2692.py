#include <iostream>
#include <string>
#include <vector>
#include <math.h>
using namespace std;

// Interpret a binary number represented by s in base i,
// and return its value. 
long long convert_base(string s, int b) {
    long long res = 0; 
    for (int i = 0; i < s.size(); i ++) {
      res += ((s[i] == '1')? 1: 0) * pow(b, (s.size() - 1 - i));
    }
    return res;
}

bool is_prime(long long n, long long& d) {
    for (long long i = 2; i <= (long long)sqrt(n); i ++) {
	if (n % i == 0) {
	    d = i;
	    return false; 
	}
    }
    return true;
}

string generate_string(int j, int N) {
    string s;
    s.push_back('1');
    for (int i = 0; i < N - 2; i ++) {
	if (j & (1 << i)) s.push_back('1');
	else s.push_back('0');
    }
    s.push_back('1');
    return s;
}

int main(int argc, char **argv) {
    int T, N, J;
    cin >> T >> N >> J;
    
    // number of different possible strings
    long long t = pow(2, N - 2); 
    
    int c = 0; // count the number of coin jams.
    cout << "Case #1:\n";
    
    long long j = 0;
    while (j < t) {
	// generate a new number as a string
	string s = generate_string(j, N);
	
	// compute the number in different bases
	bool coin_jam = true;
	vector<long long> divisors(9, -1); 
	for (int i = 2; i <= 10; i ++) {
	    long long b = convert_base(s, i);
// 	    cout << b << endl;
	    long long d; // stores the divisor.
	    
	    // check whether the number is a prime 
	    if (is_prime(b, d)) {
		coin_jam = false;
		break; 
	    }
	    else divisors[i - 2] = d;
	}
	if (coin_jam) {
	    // print and increase the count.
	    cout << s;
	    for (auto d: divisors) {
		cout << " " << d;
	    }
	    cout << "\n";
	    if (++c == J) return 0;
	}
	j ++;
    }
}
