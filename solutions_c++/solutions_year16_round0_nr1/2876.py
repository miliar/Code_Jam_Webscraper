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
	LL N;
	std::cin >> T;
	for (int t = 0; t < T; ++t) {
		std::cin >> N;
		std::cout << "Case #" << (t + 1) << ": ";
		if (N == 0) {
			std::cout << "INSOMNIA" << std::endl;
			continue;
		}
		std::vector<bool> F(10, 0);
		int nCnt = 0;
		LL M = 1;
		while (nCnt < 10) {
			LL NM = N * M;
			std::stringstream ss;
			ss << NM;
			auto s = ss.str();
			for (int j = 0; j < s.length(); ++j) F[s[j] - '0'] = 1;
			nCnt = 0;
			for (int j = 0; j < 10; ++j)  nCnt += F[j];
			M += 1;
			if (M > 1e6) break;
		}
		if (M > 1e6) {
			std::cout << "INSOMNIA" << std::endl;
			continue;
		}
		std::cout << (N*(M - 1)) << std::endl;
	}
	return 0;
}
