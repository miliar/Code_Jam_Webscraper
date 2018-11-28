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
	bool p[16];
	for(int x = 1; x <= t; ++x){

		for(int i = 0; i < 16; ++i) p[i] = false;
		for(int y = 0; y < 2; ++y) {
			int n; cin >> n;
			for(int i = 0; i < 4; ++i) {
				for(int j = 0; j < 4; ++j) {
					int k; cin >> k;
					if (i == n - 1) {
						if (y == 0) {
							p[k-1] = true;
						}
						else {
							p[k-1] = p[k-1] && true;
						}
					}
					else {
						p[k-1] = false;
					}
				}
			}
		}
		int ile = 0, res = 0;
		for (int i = 0; i < 16; ++i) {
			if (p[i]) {
				res = i+1;
				ile++;
			}
		}
		if (ile > 1) {
			cout << "Case #" << x << ": Bad magician!\n";//result 
			continue;
		}
		if (ile == 0) {
			cout << "Case #" << x << ": Volunteer cheated!\n";//result 
			continue;
		}
			cout << "Case #" << x << ": " << res<< "\n";//result 
	}
	return 0;
}
