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
void generate_prime(long limit);
#define for0(i, n) for(int i=0; i<n; i++)
#define for1(i, n) for(int i=1; i<=n; i++)	

int main() {
	std::ifstream in{ "small-practice.in" };
	std::ofstream out{ "small.out" };

	int T;
	in >> T;
	int t{ 1 };

	while (t <= T) {
		string S;
		unordered_map<char, int> map;
		vector<int> vec{};
		in >> S;

		for (auto s : S) {
			map[s]++;
		}

		int zero = map['Z'];
		int two = map['W'];
		int four = map['U'];
		int six = map['X'];
		int eight = map['G'];

		int one = map['O'] - zero - two - four;
		int five = map['F'] - four;
		int three = map['T'] - two - eight;
		int seven = map['S'] - six;
		int nine = map['I'] - five -six - eight;

		string O{};

		for1(i, zero) {
			O += "0";
		}

		for1(i, one) {
			O += "1";
		}

		for1(i, two) {
			O += "2";
		}

		for1(i, three) {
			O += "3";
		}

		for1(i, four) {
			O += "4";
		}

		for1(i, five) {
			O += "5";
		}

		for1(i, six) {
			O += "6";
		}

		for1(i, seven) {
			O += "7";
		}

		for1(i, eight) {
			O += "8";
		}

		for1(i, nine) {
			O += "9";
		}

		out << "Case #" << t << ": " << O << std::endl;
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

bool is_prime(long n) {
	return binary_search(primes.begin(), primes.end(), n);
}

bool is_dyn_prime(long n) {
	long root = static_cast<long>(sqrt(n)) + 2; //I don't want issues with precision
	for (size_t K = 0; K<primes.size() && primes[K]<root; ++K)
		if (n%primes[K] == 0)
			return false;
	return true;
}

void generate_prime(long limit) {
	if (limit >= 2)
		primes.push_back(2);
	for (long K = 3; K <= limit; K += 2)
		if (is_dyn_prime(K))
			primes.push_back(K);
}