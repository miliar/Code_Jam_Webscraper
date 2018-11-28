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
#include<vector>
using namespace std;

typedef long long LL;
typedef long double LD;

#define dprintf(...) fprintf(stderr, __VA_ARGS__)

int cond = 1;
#define DB(X) {if(cond){cerr<<"Line:"<<__LINE__<<", "<<#X<<" = "<<X<<endl;}}
int main() {
	int t; cin >> t;
	for(int x = 1; x <= t; ++x){
			int sm; cin >> sm;
			string s; cin >> s;
			int res = 0, is = 0;
			for (int i = 0; i <= sm; ++i) {
				int no = s[i] - '0';
				if (is < i) {
					res += i - is;
					is += i - is;
				}
				is += no;  
			}

			cout << "Case #" << x << ": " << res<< "\n";//result 
	}
	return 0;
}
