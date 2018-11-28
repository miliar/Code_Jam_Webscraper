#include <iostream>
#include <algorithm>
#include <list>
#include <cmath>
#include <vector>
#include <string>
#include <cstring>
#include <climits>
#include <cstdio>
#include <set>
#include <map>
using namespace std;

#define forn(a,n) for(int a = 0; a<(n); ++a)
#define forsn(a,s,n) for(int a = (s); a<(n); ++a)
#define forall(a,all) for(__typeof(all.begin()) a = all.begin(); a != all.end(); ++a)

typedef long long tint;

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T, n;
	string opera;

	cin >> T;
	forn(t, T) {
		cin >> n >> opera;
		int ret = 0, aplaudiendo = opera[0]-'0';
		forsn(i, 1, opera.size()) {
			if(aplaudiendo < i) {
				ret += i-aplaudiendo;
				aplaudiendo = i;
			}
			aplaudiendo += opera[i]-'0';
		}
		printf("Case #%i: %i\n", t+1, ret);
	}

	return 0;
}
