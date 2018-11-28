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

std::ifstream in{ "small-practice.in" };
std::ofstream out{ "small.out" };

long solve(int N) {
	
	return 0;
}

int main() {
	

	int T;
	in >> T;
	int t{ 1 };

	while (t <= T) {
		int N;
		in >> N;

		unordered_map<int, int> map{};

		for (int i = 1; i <= 2*N - 1; i++) {
			for (int j = 0; j < N; j++) {
				int height;
				in >> height;
				map[height]++;
			}
		}

		vector<int> list{};

		for (auto height : map) {
			if (height.second % 2 != 0) {
				list.push_back(height.first);
			}

		}

		sort(list.begin(), list.end());

		out << "Case #" << t << ": ";
		
		for (auto height : list) {
			out << height << " ";
		}

		out << std::endl;

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