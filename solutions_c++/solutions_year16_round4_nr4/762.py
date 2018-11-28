#include <cstdio>
#include <cmath>
#include <cstring>
#include <iostream>
#include <iomanip>
#include <set>
#include <stack>
#include <map>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;

const int NMAX = 100000 + 7;
const int INF = 1000000000;

char a[5][5];
bool solved;
int mn;

int busy[5];
int can[5][5];


int ok4Count = 131;
int ok4[10000] = {4680, 4740, 4812, 5160, 5250, 5290, 5736, 5766, 6180, 6210, 6246, 6730, 6820, 7212, 7362, 7918, 8520, 8580, 8652, 9240, 9345, 9369, 9560, 9605, 10260, 10305, 10325, 10569, 10644, 11292, 11457, 11741, 13128, 13188, 13260, 13368, 13443, 14388, 14403, 15420, 15555, 16680, 16770, 16810, 16920, 17025, 17049, 17208, 17283, 18450, 18465, 18483, 18729, 18834, 18970, 19105, 19387, 21080, 21125, 21800, 21890, 21930, 22565, 22610, 23130, 23205, 24936, 24966, 26136, 26241, 26265, 26646, 26721, 26985, 27030, 30584, 30599, 30839, 33060, 33090, 33126, 33300, 33345, 33365, 33588, 33603, 33810, 33825, 33843, 34085, 34130, 34326, 34401, 34679, 37449, 37524, 37929, 38034, 38505, 38550, 39204, 39234, 39270, 41290, 41380, 42010, 42145, 42330, 42405, 43540, 43585, 43605, 46267, 47947, 48052, 49452, 49602, 49692, 49857, 49980, 50115, 52242, 52257, 52275, 53981, 56621, 56786, 57838, 60958, 61153, 65535};

bool canTake(int n, int cur) {
	if (cur == n) {
		return true;
	}
	bool hasOne = false;
	bool ok = true;
	for (int j=0;j<n;j++) {
		if (!busy[j] && can[cur][j]) {
			hasOne = true;
			busy[j] = true;
			ok &= canTake(n,cur+1);
			busy[j] = false;
		}
	}
	if (!hasOne) {
		return false;
	}
	return ok;
}

bool test(int n) {
	vector <int> per;
	for (int i=0;i<n;i++) {
		per.push_back(i);
	}
	int fact = 1;
	for (int i=1;i<=n;i++) {
		fact *= i;
	}
	for (int perm=0;perm<fact;perm++) {

		for (int i=0;i<n;i++) {
			for (int j=0;j<n;j++) {
				can[i][j] = (a[per[i]][j] != '0');
				busy[j] = 0;
			}
		}

		if (!canTake(n,0)) {
			return false;
		}

		next_permutation(per.begin(),per.end());
	}
	return true;
}

void solve(int n, int li, int lj) {

	if (4 == n) {
		for (int k=0; k < ok4Count; k++) {
			int cur = 0;
			for (int i=0;i<n;i++) {
				for (int j=0;j<n;j++) {
					bool need = (((1 << (i*n+j)) & ok4[k]) > 0);
					if (!need && a[i][j] == '1') {
						cur = INF;
					}
					if (a[i][j] == '0' && need) {
						cur++;
					}
				}
			}
			mn = min(mn,cur);
		}
		return; 
	}

	if (test(n)) {
		int cur = 0;
		for (int i=0;i<n;i++) {
			for (int j=0;j<n;j++) {
				if (a[i][j] == '2') {
					cur++;
				}
			}
		}
		mn = min(mn,cur);
		return ;
	}

	for (int i=li;i<n;i++) {
		for (int j=((i==li)?lj:0);j<n;j++) {
			solve(n,i,j+1);
			if (a[i][j] == '0') {
				a[i][j] = '2';
				solve(n,i,j+1);
				a[i][j] = '0';
			}
		}
	}
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;

	cin >> t;
	for (int testNumber = 1; testNumber <= t; testNumber++) {
		cout << "Case #" << testNumber << ": ";
		int n;
		cin >> n;
		for (int i=0;i<n;i++) {
			for (int j=0;j<n;j++) {
				cin >> a[i][j];
			}
		}		

		int mask = 0;

		for (int i=0;i<n;i++) {
			for (int j=0;j<n;j++) {
				if (a[i][j] == '1') {
					mask |= (1 << (i * n + j));
				}
			}
		}
		mn = INF;
		solve(n,0,0);
		cout << mn;

		cout << endl;
	}
	return 0;
}