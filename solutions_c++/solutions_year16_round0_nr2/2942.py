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

#define MAX_N 101
struct TStck {
	int stck[MAX_N];
	int len;
} ;

int Flip(int* stck, int len, int flipslen, int& bres) {
	if (flipslen >= bres) return bres;
	if (len == 1) {
		if (stck[0] > 0) return flipslen;
		else return flipslen + 1;
	}
	TStck tmpstck;
	for (int j = 1; j < len; ++j) {
		if (stck[j] * stck[0] < 0) {
			int l = 0;
			for (int k = j-1; k>0; --k)
				tmpstck.stck[l++] = -stck[k];
			tmpstck.stck[l++] = -stck[0] + stck[j];
			for (int k = j+1; k < len; ++k)
				tmpstck.stck[l++] = stck[k];
			tmpstck.len = l;
			return Flip(tmpstck.stck, tmpstck.len, flipslen + 1, bres);
			//int nbres = Flip(tmpstck.stck, tmpstck.len, flipslen + 1, bres);
			//bres = nbres;
		}
	}
	return bres;
}

int main()
{
	int T;
	LL N;
	std::cin >> T;
	for (int t = 0; t < T; ++t) {
		std::cout << "Case #" << (t + 1) << ": ";
		std::string s;
		std::cin >> s;
		std::vector<int> stck;
		int lst = 0;
		for (int i = 0; i < s.length(); ++i) {
			if (s[i] == '+' && lst <= 0) {
				if (lst < 0) stck.push_back(lst);
				lst = 1;
			} else if (s[i] == '+' && lst >= 0) {
				lst += 1;
			}
			else if (s[i] == '-' && lst >= 0) {
				if (lst > 0) stck.push_back(lst);
				lst = -1;
			} else {
				lst -= 1;
			}
		}
		if (lst != 0) stck.push_back(lst);
		auto N = stck.size();
		int bres = MAX_N + 1;
		//std::cout << N << "  ";
		std::cout << Flip(&*stck.begin(), N, 0, bres) << std::endl;
	}
	return 0;
}
