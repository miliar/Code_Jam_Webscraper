#include <stdio.h>
#include <limits.h>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <functional>
#include <string>

#define MAX_N 64
#define ALL(a) (a).begin(),(a).end()
#define SZ(a) int((a).size())
#define dump(x) cout << #x << " = " << (x) << endl;
#define debug(x) cout << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;

using namespace std;
typedef long long LL;

inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}

int main() {
	int testcaseNum;
	cin >> testcaseNum;
	for(int testcaseIndex = 0; testcaseIndex < testcaseNum; ++testcaseIndex){
		LL ans = 0;

		// input
		int x;
		int n;
		cin >> n;
		cin >> x;
		vector<int> prob;
		for(int i = 0; i < n; ++i){
			int s;
			cin >> s;
			prob.push_back(s);
		}

		// solve
		sort(ALL(prob), greater<int>());
		int begin = 0;
		int end = (int)(prob.size() - 1);
		while(begin <= end){
			if((prob[begin] + prob[end]) <= x){
				++begin;
				--end;
				++ans;
			} else {
				++begin;
				++ans;
			}
		}

		printf("Case #%d: %lld\n", testcaseIndex+1, ans);
	}

	return 0;
}
