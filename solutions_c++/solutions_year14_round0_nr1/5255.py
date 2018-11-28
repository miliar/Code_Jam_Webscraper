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

int kol[22];
int a[5][5], b[5][5];
int x, y;

int main(){
	freopen("1.in","r",stdin);	
	freopen("1.out","w",stdout);
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt++) {
		cin >> x;
		for (int i = 0; i < 4; i++) for (int j = 0; j < 4; j++) cin >> a[i][j];
		cin >> y;
		for (int i = 0; i < 4; i++) for (int j = 0; j < 4; j++) cin >> b[i][j];
		for (int i = 0; i <= 16; i++) kol[i] = 0;
		for (int i = 0; i < 4; i++) kol[a[x - 1][i]]++;
		for (int i = 0; i < 4; i++) kol[b[y - 1][i]]++;
		vector<int> ans;
		for (int i = 1; i <= 16; i++) if (kol[i] == 2) ans.pb(i);
		cout << "Case #" << tt << ": ";
		if (ans.size() == 0) puts("Volunteer cheated!"); else
		if (ans.size() > 1) puts("Bad magician!"); else cout << ans[0] << endl;

	}
	return 0;
}