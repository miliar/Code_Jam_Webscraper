#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <vector>
#include <stack>
#include <algorithm>
#define MOD 1000000007
#define forn(a, n) for(int a = 0; a<(int) (n); ++a)
#define dforn(a, n) for(int a = (n)-1; a>=0; --a)
#define forall(a, all) for(__typeof(all.begin()) a = all.begin(); a != all.end(); ++a)
#define EPS 0.000000000001
typedef long long tint;
using namespace std;

long long flip[18];

tint inv(int n)
{
	tint ans=0;
	while(n>0)
	{
		ans*=10;
		ans+=n%10;
		n/=10;
	}
	return ans;
}

int main()
{
#ifdef ACMTUYO
	freopen("A-large(3).in","r",stdin);
	freopen("A-large(3).out","w",stdout);
#endif
	
	int C;
	cin >> C;
	forn(tc, C) {
		int k;
		string p;
		cin >> p >> k;
		
		int ans = 0;
		forn(i, p.size()) {
			if(p[i] == '-') {
				if(i+k <= (int) p.size()) {
					forn(j, k) {
						if(p[i+j] == '-') {
							p[i+j] = '+';
						} else {
							p[i+j] = '-';
						}
					}
					ans++;
				} else {
					ans = -1;
				}
			}
		}
		cout << "Case #" << tc+1 << ": "; 
		if(ans>=0) {
			cout << ans;
		} else {
			cout << "IMPOSSIBLE";
		}
		cout << endl;
	}
	
	return 0;
}
