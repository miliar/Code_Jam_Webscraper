#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <set>
#include <iomanip>
#include <map>
#include <queue>
#include <ctime>
#include <stack>
#include <bitset>

#define X first
#define Y second
#define pb push_back
#define mp make_pair
#define sqr(x) ((x)*(x))
#define bitcnt(x) __builtin_popcountll(x)
#define rt return

typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;

using namespace std;

const int INF = (int)1e9 + 37;
const double PI = acos(-1.0);
const int MAXN = 101;

const int dx[4] = {0, -1, 0, 1};
const int dy[4] = {-1, 0, 1, 0};
const char dir[4] = {'L', 'U', 'R', 'D'};

string inverse(string s, int x){
	string ret = s;
	for (int i=0;i<=x;i++){
		s[i] == '-' ? ret[i] = '+' : ret[i] = '-';	
	}
	return ret;
}

bool isOK(string s){
	for (int i=0;i<(int)s.length();i++){
		if (s[i] == '-'){
			return 0;
		}
	}
	return 1;
}

int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	
	int T;
	cin >> T;
	for (int j=1;j<=T;j++){
		string s;
		cin >> s;
		int ans = 0;
		for (int i=(int)s.length() - 1;i>=0;i--){
			if (s[i] == '-'){
				s = inverse(s, i);
				ans++;
			}
		}
				
		printf("Case #%d: %d\n", j, ans);
	}
	
	
	
    rt 0;
}
