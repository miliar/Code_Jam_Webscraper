#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>

#define all(v)          v.begin(),v.end()
#define allr(v)         v.rbegin(),v.rend()
#define rep(i,m)        for(int i=0;i<(int)m;i++)
#define REP(i,k,m)      for(int i=k;i<(int)m;i++)
#define mem(a,b)        memset(a,b,sizeof(a))
#define mp              make_pair
#define pb              push_back

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef vector<pair<int, int> > vpii;

int diri[] = { -1, 0, 1, 0, -1, 1, 1, -1 };
int dirj[] = { 0, 1, 0, -1, 1, 1, -1, -1 };

#define OO ((ll)1e14)
#define MAX 100000
string res;
void f(int num) {
	if (num == 0)
		return;
	f(num / 10);
	res += num % 10 + '0';
}
bool pal(string s) {
	if (s.size() == 1)
		return true;
	for (int i = 0; i < s.size()/2; ++i) {
		if (s[i] != s[s.size() - 1])
			return false;
	}
	return true;
}
int main() {
	freopen ("C-small-attempt0.in","r+",stdin);
	freopen ("out2.txt","w+",stdout);
	int t;
	cin >> t;
	int a, b;
	bool x, y;
	int k = 1;
	while (t--) {
		int rs = 0;
		cin >> a >> b;
		for (int i = a; i <= b; ++i) {
			res ="" ;
			f(i);
			x = pal(res);
			res = "";
			int ss = sqrt(i);
			if (i  == ss*ss) {
				f(ss);
				y = pal(res);
			}
			else
				y = false ;
			if (x && y){
				rs++;
			}
		}
		printf("Case #%d: %d\n",k,rs);
		k++;
	}
	return 0;
}
