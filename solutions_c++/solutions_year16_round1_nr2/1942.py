#include <cstdio>
#include <iostream>
#include <string>
#include <sstream>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <random>

using namespace std;

typedef long long LL;
typedef long double LD;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int,int> PII;
#define FOR(k,a,b) for(typeof(a) k=(a); k <= (b); ++k)
#define REP(k,a) for(int k=0; k < (a); ++k)
#define REPD(k,a) for(int k=(a)-1; k >= 0; --k)
#define PB push_back 
#define MP make_pair

int main()
{
	int T;
	std::cin >> T;
	LL N;
	int m[2501];
	for (int t = 0; t < T; ++t) {
		std::cout << "Case #" << (t + 1) << ": ";
		std::cin >> N;
		memset(m, 0, sizeof(int) * 2501);
		for (int i = 0; i < 2 * N - 1; i++) {
			for (int j = 0; j < N; ++j) {
				int v;
				std::cin >> v;
				m[v] += 1;
			}
		}
		for (int i = 0; i < 2501; ++i) {
			if (m[i] % 2 == 1) std::cout << i << " ";
		}
		std::cout << std::endl;
	}
	return 0;
}
