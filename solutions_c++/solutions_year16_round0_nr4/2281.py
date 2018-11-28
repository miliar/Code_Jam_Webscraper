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
	LL K,C,S;
	std::cin >> T;
	for (int t = 0; t < T; ++t) {
		std::cout << "Case #" << (t + 1) << ": ";
		std::cin >> K >> C >> S;
		for (int j = 0; j < K; ++j) {
			LL nPos = j;
			for (LL i = 1; i < C; ++i) {
				nPos = nPos * K + j;
			}
			std::cout << (nPos + 1) << " ";
		}
		std::cout << std::endl;
	}
	return 0;
}
