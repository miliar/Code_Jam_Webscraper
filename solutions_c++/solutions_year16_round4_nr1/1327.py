/**************************************************
 * Author	 : xiaohao Z
 * Blog	 : http://www.cnblogs.com/shu-xiaohao/
 * Last modified : 2016-05-28 21:43
 * Filename	 : A.cpp
 * Description	 : 
 * ************************************************/

#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <cmath>
#include <algorithm>
#include <queue>
#include <stack>
#include <vector>
#include <set>
#include <map>
#define MP(a, b) make_pair(a, b)
#define PB(a) push_back(a)

using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<unsigned int,unsigned int> puu;
typedef pair<pii, int> piii;
typedef pair<ll, int> pli;
typedef pair<int, ll> pil;

const int INF = 0x3f3f3f3f;
const double eps = 1E-6;
int num[15][3][3], n, R, P, S;
string str[3] = {"P", "R", "S"};
set<piii> s;

piii mp(int a, int b, int c) {
	return MP(MP(a, b), c);
}

void getn(int l, int pos) {
	num[l + 1][pos][0] = num[l][pos][0] + num[l][pos][2];
	num[l + 1][pos][1] = num[l][pos][0] + num[l][pos][1];
	num[l + 1][pos][2] = num[l][pos][1] + num[l][pos][2];
}

void init() {
	s.clear();
	memset(num, 0, sizeof num);
	num[0][0][0] = num[0][1][1] = num[0][2][2] = 1;
	for(int i=0; i<14; i++) 
		for(int j=0; j<3; j++) getn(i, j);
}

bool J(int pos) {
	if(P != num[n][pos][0]) return false;
	if(R != num[n][pos][1]) return false;
	if(S != num[n][pos][2]) return false;
	return true;
}

string devided(int l, int pos) {
	if(l == 0) {
		string ret = str[pos];
		return ret;
	}
	string A, B;
	if(pos == 0){
		A = devided(l - 1, 0);
		B = devided(l - 1, 1);
	}else if(pos == 1) {
		A = devided(l - 1, 1);
		B = devided(l - 1, 2);
	}else if(pos == 2) {
		A = devided(l - 1, 0);
		B = devided(l - 1, 2);
	}
	return (A > B ? B + A : A + B);
}

bool solve() {
	for(int i=0; i<3; i++) if(J(i)){
		string ans = devided(n, i);
		cout << ans;
		return true;
	}
	return false;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	init();
	int T, kase = 1;
	cin >> T;
	while(T --) {
		cin >> n >> R >> P >> S;
		cout << "Case #" << kase ++ << ": ";
		if(solve()) {
			cout << endl;
		}else cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}

