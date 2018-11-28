#include<algorithm>
#include<cassert>
#include<cctype>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<deque>
#include<iostream>
#include<list>
#include<map>
#include<queue>
#include<set>
#include<string>
#include<sstream>
#include<vector>
using namespace std;

typedef long long LL;
typedef long double LD;

#define dprintf(...) fprintf(stderr, __VA_ARGS__)

int cond = 1;
#define DB(X) {if(cond){cerr<<"Line:"<<__LINE__<<", "<<#X<<" = "<<X<<endl;}}

string solve() {
	int n; cin >> n;
	if (n == 0) {
		return "INSOMNIA";
	}
	set<char> d;
	long long j = 0LL;
	string s;
	while (d.size() < 10) {
		j += n;
		s = static_cast<ostringstream*>( &(ostringstream() << j) )->str();
		for(char c : s) {
			d.insert(c);
		}
	}
	return s;
}

int main() {
	int t; cin >> t;
	for(int x = 1; x <= t; ++x){
		cout << "Case #" << x << ": " << solve() << endl;//result 
	}
	return 0;
}
