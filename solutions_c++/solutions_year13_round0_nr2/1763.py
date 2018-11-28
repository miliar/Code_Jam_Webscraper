
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cmath>
#include<cstdlib>
#include<queue>
#include<map>
#include<set>
#include<string>
#include<sstream>
#include<climits>
#include<vector>
#include<cstring>
#include<stack>

using namespace std;

#define REP(i,s,n)  for (int i=(s),_n=(n);i<=_n;i++)
#define FOR(i,s,n)  for (int i=(s),_n=(n);i<_n;i++)
#define REPD(i,e,s)  for (int i=(e),_s=(s);i>=_s;i--)
#define tr(container, it) \
	for (typeof(container.begin()) it=container.begin(); it!=container.end();it++)
#define PB push_back
#define MP make_pair

typedef long long LL;

int ar[200][200];

int n,m;
bool check(int x,int y) {
	int val=ar[x][y];
	int f=1;
	REP(i,1,n) if (ar[i][y]>val) {
		f=0;
		break;
	}
	if (f) return true;
	f=1;
	REP(i,1,m) if (ar[x][i]>val) {
		f=0;
		break;
	}
	if (f) return true;
	return false;
}

int main() {
	int t;
	cin >> t;
	REP(tc,1,t) {
		memset(ar,0,sizeof ar);
		cin >> n >> m;
		int flag=0;
		REP(i,1,n) REP(j,1,m) cin >> ar[i][j];
		REP(i,1,n) {
			REP(j,1,m) {
				if (!check(i,j)) {
					flag=1;
					break;
				}
			}
			if (flag) break;
		}
		if (flag==0) cout << "Case #" << tc << ": YES" << endl;
		else cout << "Case #" << tc << ": NO" << endl;
	}
	return 0;
}
