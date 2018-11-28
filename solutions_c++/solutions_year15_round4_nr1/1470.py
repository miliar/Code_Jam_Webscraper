#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<string.h>
#include<cmath>
#include<cassert>
using namespace std;

#define SMALL 1
#define LARGE 1

char a[2000][2000];
bool b[1010][1010];

string s = "<>^v";

int getInd(char c) {
	int ans = find(s.begin(), s.end(), c)-s.begin();
	assert(ans >=0 && ans < 4);
	return ans;
}

int main() {
#ifdef LARGE
	freopen("a_large.i", "rt", stdin);
	freopen("a_large.o", "wt", stdout);
#elif SMALL
	freopen("a_small_2.i", "rt", stdin);
	freopen("a_small_2.o", "wt", stdout);
#else
	freopen("a_sample.i", "rt", stdin);
#endif

	int t;
	cin>>t;
	for(int tt=1;tt<=t;tt++) {
		int r,c;
		cin>>r>>c;
		for(int i=0;i<r;i++)
			for(int j=0;j<c;j++)
				cin>>a[i][j];

		memset(b, 0, sizeof(b));
		int ans = 0;
		for(int i=0;i<r;i++) {
			bool last = 0;
			for(int j=0;j<c;j++) {
				b[i][j] = b[i][j] || last;
				if(!last && a[i][j] != '.' && getInd(a[i][j]) == 0) {
					ans++;
				}
				last = last || (a[i][j] != '.');
			}
		}

		for(int i=0;i<r;i++) {
			bool last = 0;
			for(int j=c-1;j>=0;j--) {
				b[i][j] = b[i][j] || last;
				if(!last && a[i][j] != '.' && getInd(a[i][j]) == 1) {
					ans++;
				}
				last = last || (a[i][j] != '.');
			}
		}

		for(int j=0;j<c;j++) {
			bool last = 0;
			for(int i=0;i<r;i++) {
				b[i][j] = b[i][j] || last;
				if(!last && a[i][j] != '.' && getInd(a[i][j]) == 2) {
					ans++;
				}
				last = last || (a[i][j] != '.');
			}
		}

		for(int j=0;j<c;j++) {
			bool last = 0;
			for(int i=r-1;i>=0;i--) {
				b[i][j] = b[i][j] || last;
				if(!last && a[i][j] != '.' && getInd(a[i][j]) == 3) {
					ans++;
				}
				last = last || (a[i][j] != '.');
			}
		}

		bool imp = false;
		for(int i=0;i<r;i++)
			for(int j=0;j<c;j++) {
				if(a[i][j] == '.') continue;
				if(!b[i][j]) imp = true;
			}

		if(imp)
			cout << "Case #"<<tt<<": IMPOSSIBLE"<<endl;
		else
			cout << "Case #"<<tt<<": "<<ans<<endl;
	}

	return 0;
}
