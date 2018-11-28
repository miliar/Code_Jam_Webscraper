// very useful, common imports
#include <iostream>
#include <string>
#include <stdlib.h>
#include <memory>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cctype>
#include <vector>
#include <map>
#include <list>
#include <deque>
#include <algorithm>
#include <cmath>
#include <fstream>
#include <set>
#include <bitset>
//#include <boost/dynamic_bitset.hpp>

// bost library for printing out complex data structs. useful for debugging
// can be found http://louisdx.github.io/cxx-prettyprint/
#include "../common/prettyprint.h"

#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)
#define mp make_pair
#define pb push_back
#define all(v) v.begin(),v.end()
#define sz size()

using namespace std;

using pii = pair<int, int>;
using vpii = vector<pii>;
using vi = vector<int>;
using vd = vector<double>;
using vii = vector<vector<int> >;

set<long long> primes;

static void populate_primes()
{
	for (int i = 1; i < 4; ++i) {
		string fname = "primes" + to_string(i) + ".txt";
	    ifstream infile(fname);
	    assert(infile.good());
	    long prime;
	    while (infile >> prime) {
	        primes.insert(prime);
	    }
	}
}

void print_jam(int length, long long num)
{
	// grab bin repr
	string binstr = bitset<32>(num).to_string();

	string finalstr = binstr.substr(32 - length, length);

	cout << finalstr << " ";

	for (int base = 2; base < 11; ++base) {
		long long n = strtoll(binstr.c_str(), nullptr, base);

		for (long long i = 2; ; ++i) {
			if (n % i == 0) {
				cout << i << " ";
				break;
			}
		}
	}

	cout << "\n";
}

bool is_prime(long long num)
{
	for(int i=2; i <= sqrt(num) ;++i) {
      if(num % i==0){
          return false;
      }
  	}
  	return true;
}

bool is_jam(int length, long long num)
{
	// grab bin repr
	string binstr = bitset<32>(num).to_string();

	string finalstr = binstr.substr(32 - length, length);

	if (finalstr[0] == '0') return false;
	if (finalstr[finalstr.length() - 1] == '0') return false;

	for (int base = 2; base < 11; ++base) {
		long long n = strtoll(finalstr.c_str(), nullptr, base);
		if (n > 49979687) {
			if (is_prime(n)) {
				return false;
			}
		}
		else if (primes.find(n) != primes.end()) {
			return false;
		}
	}

	return true;
}

void solve(int n)
{
	cout << "Case #" << n << ":\n";
	int length, num_to_gen;
	cin >> length >> num_to_gen;

	int num_gen = 0;
	string start_num = "1";
	for (int i = 0; i < length - 2; ++i) start_num += '0';
	start_num += '1';

	long long it = strtoll(start_num.c_str(), nullptr, 2);

	while (num_gen < num_to_gen) {
		
		// checks and prints if it is
		if (is_jam(length, it)) {
			print_jam(length, it);
			num_gen++;
		}

		it++;
	}
}

int main()
{
	populate_primes();
	int N;
	cin >> N;

	for (int i = 0; i < N; ++i) {
		solve(i+1);
	}
}