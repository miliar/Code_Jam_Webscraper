#include<stdio.h>
#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
#include<memory.h>
#include<map>
#include<set>
#include<queue>
#include<list>
#include<sstream>
#define mp make_pair
#define pb push_back      
#define F first
#define S second
#define SS stringstream
#define sqr(x) ((x)*(x))
#define m0(x) memset(x,0,sizeof(x))
#define m1(x) memset(x,63,sizeof(x))
#define CC(x) cout << (x) << endl
#define pw(x) (1ll<<(x))
#define M 1000000007
#define N 111111
using namespace std;
typedef pair<int,int> pt;

int n, L;
string g[111], bad;


int main(){
	freopen("1.in","r",stdin);	
	freopen("1.out","w",stdout);
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt++) {
		cout << "Case #" << tt << ": ";
		cin >> n >> L;
		for (int i = 0; i < n; i++) cin >> g[i];
		cin >> bad;

		int ba = 0;
		for (int i = 0; i < n; i++) if (g[i] == bad) ba = 1;
		if (ba) {
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		if (L == 1) {
			cout << "0?" << " 0" << endl;
			continue;
		}


		string p1 = "";
		string p2 = "";
		for (int i = 0; i < L; i++) p1 += "0?";
		for (int i = 0; i < L - 1; i++) p2 += "1";


		cout << p1 << " " << p2 << endl;

	}
	return 0;
}