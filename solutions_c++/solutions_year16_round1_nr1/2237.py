#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <stack>
#include <queue>
#include <unordered_map>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <set>
#include <numeric>

using namespace std;

int gcd(int a, int b);
int lcm(int a, int b);
int lcm(vector<int> arr);
bool is_prime(long n);
bool is_dyn_prime(long n);
void generate_prime( long limit );

string solve(string S) {
	string Smax = "";
	int N = S.size();

	Smax += S.substr(0, 1);
	for (int i = 1; i < S.size(); i++) {
		string Smax1 = Smax + S.substr(i, 1);
		string Smax2 = S.substr(i, 1) + Smax;

		Smax = Smax1;

		for (int j = 0; i <= i; j++) {
			if (Smax1[j] > Smax2[j]) {
				Smax = Smax1;
				break;
			}
			else if (Smax1[j] < Smax2[j]) {
				Smax = Smax2;
				break;
			}

		}
	}

	/*	
	for (int i = 1; i <= S.size(); i++) {
		int start = (N-i > i-1) ? 1 : i;
		start = (start >= 1) ? start : 1;

		int end = N - i + 1;
		end = (end >= i) ? end : i;

		char max = S[start-1];
		int maxPos = start;

		for (int j = start; j <= end; j++) {
			if (S[j-1] > max) {
				max = S[j-1];
				maxPos = j;
			}
		}

		Smax[i-1] = S[maxPos-1];
		S[maxPos-1] = 32;
	}	
	*/
	return Smax;
}

int main() {
	std::ifstream in{ "small-practice.in" };
	std::ofstream out{ "small.out" };

	int T;
	in >> T;
	int t{ 1 };
	 
	while (t <= T) {
		string S;
		in >> S;

		out << "Case #" << t << ": " << solve(S) << std::endl;
		t++;
	}

	return 0;
}

int gcd(int a, int b)
{
	for (;;)
	{
		if (a == 0) return b;
		b %= a;
		if (b == 0) return a;
		a %= b;
	}
}

int lcm(int a, int b)
{
	int temp = gcd(a, b);

	return temp ? (a / temp * b) : 0;
}

/*
int lcm(vector<int> arr) {
	accumulate(arr.begin(), arr.end(), 1, [](int a, int b) {
										return lcm(a, b);});
}
*/
std::vector<long> primes;

bool is_prime(long n){
	return binary_search(primes.begin(), primes.end(), n);
}

bool is_dyn_prime(long n){
	long root = static_cast<long>(sqrt(n)) + 2; //I don't want issues with precision
	for(size_t K=0; K<primes.size() && primes[K]<root; ++K)
		if(n%primes[K] == 0) 
			return false;
	return true;
}

void generate_prime( long limit ){
	if( limit>=2 )
		primes.push_back(2);
	for(long K=3; K<=limit; K+=2)
		if( is_dyn_prime(K) )
			primes.push_back(K);
}