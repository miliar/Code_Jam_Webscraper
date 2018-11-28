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

void Solve(const std::vector< std::pair<int, char> >& s) {
	std::string res = "";
	if (s.size() == 0) return;
	if (s.size() == 1) {
		std::cout << s[0].second;
		return;
	}
	int mid = s[0].first;
	std::vector< std::pair<int, char> > s1;
	std::vector< std::pair<int, char> > s2;
	for (int i = 1; i < s.size(); ++i) {
		if (s[i].first < mid) s1.push_back(s[i]);
		if (s[i].first > mid) s2.push_back(s[i]);
	}
	std::cout << s[0].second;
	Solve(s1);
	std::sort(s2.begin(), s2.end(), [](const pair<int, char>& a, const pair<int, char>& b){return a.first < b.first; });
	for (int i = 0; i < s2.size(); ++i) std::cout << s2[i].second;
}

int main()
{
	int T;
	std::cin >> T;
	std::string S;
	
	for (int t = 0; t < T; ++t) {
		std::cout << "Case #" << (t + 1) << ": ";
		std::cin >> S;
		std::vector< std::pair<int, char> > s;
		for (auto i = 0; i < S.size(); ++i) s.push_back(make_pair(i, S[i]));
		//for (int i = 0; i < s.size(); ++i) {
		//	std::cout << s[i].first << " : " << s[i].second << std::endl;
		//}
		std::sort(s.begin(), s.end(), [](const pair<int, char>& a, const pair<int, char>& b) {return a.second > b.second || (a.second == b.second && a.first > b.first); });
		Solve(s);
		std::cout << std::endl;
		//std::cout << Solve(s) << std::endl;
	}
	return 0;
}
