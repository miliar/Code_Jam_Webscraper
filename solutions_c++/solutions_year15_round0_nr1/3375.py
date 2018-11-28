#include <iostream>
#include <ctime>
#include <fstream>
#include <cmath>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <complex>
#include <utility>
#include <cctype>
#include <list>
#include <bitset>

using namespace std;

#define FORALL(i,a,b) for(int i=(a);i<=(b);++i)
#define FOR(i,n) for(int i=0;i<(n);++i)
#define FORB(i,a,b) for(int i=(a);i>=(b);--i)

typedef long long ll;
typedef long double ld;
typedef complex<ld> vec;

typedef pair<int,int> pii;
typedef map<int,int> mii;

#define pb push_back
#define mp make_pair

#define MAXN 2000
char T[MAXN];

int main() {
	int TEST,N;
	scanf("%d",&TEST);
	FOR(test,TEST) {
		scanf("%d%s",&N,&T[0]);
		int ans = 0;
		int people_standing = 0;
		FORALL(need,0,N) {
			if (T[need] == '0') continue;
			
			// if people_standing < need, add some more people
			int add = max(0, need - people_standing);
			people_standing += add;
			ans += add;
			assert(people_standing >= need);
			people_standing += (int)(T[need]-'0');
		}
		printf("Case #%d: %d\n", (test+1), ans);
	}
}















