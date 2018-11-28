#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <bitset>
#include <map>
#include <set>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <string>
#include <sstream>
#define INF 1000000000
#define INFll 1000000000000000000ll
#define LD long double
#define LL long long
#define Vi vector<int>
#define VI Vi::iterator
#define Si set<int>
#define SI Si::iterator
#define Mi map<int, int>
#define MI Mi::iterator
#define Li list<int>
#define LI Li::iterator
#define pb push_back
#define mp make_pair
using namespace std;

int tst, r, n, m, k, a[7], f[3];

bool check(){
	int msk = 0;
	for (int i = 0; i < 8; i++){
		int now = 1;
		for (int j = 0; j < 3; j++)
			if (i & (1 << j))
				now *= f[j];
		for (int j = 0; j < 7; j++)
			if (a[j] == now)
				msk |= (1 << j);
	}
	return msk == (1 << 7) - 1;
}

void solve(){
	for (int i = 0; i < 7; i++)
		cin >> a[i];
	for (f[0] = 2; f[0] <= 5; f[0]++)
		for (f[1] = f[0]; f[1] <= 5; f[1]++)
			for (f[2] = f[1]; f[2] <= 5; f[2]++)
				if (check()){
					cout << f[0] << f[1] << f[2] << endl;
					return;
				}
}

int main(){
	cin >> tst;
	cout << "Case #1:" << endl;
	cin >> r >> n >> m >> k;
	for (int i = 0; i < r; i++)
		solve();
	return 0;
}






