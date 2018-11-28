
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cstring>
#include <memory.h>
#include <cassert>

using namespace std;

#define ford(i, a, b, c)        for(int i=(a); i<(b); i+=(c))
#define fori(i, a, b)           ford(i,a,b,1)
#define rep(i, n)               fori(i,0,n)
#define ifor(i, a, b)           for(int i=(a); i>=(b); i--)
#define iter(i, a)              for(typeof(a.begin()) i=(a).begin(); i!=(a).end(); i++)
#define si(x)                   ((int)x.size())
#define SS                      ({int x;scanf("%d",&x);x;})
#define pb                      push_back
#define mp                      make_pair
#define all(a)                  a.begin(),a.end()
#define fill(a, v)              memset(a, v, sizeof(a))
#define inf                     (int)1e9
#define linf                    (long long)1e18
#define V                       vector
#define S                       string
#define XX                      first
#define YY                      second
#define P(v)                    rep(i, si(v)) cout<<v[i]<<" "; puts("")

typedef V<int> vi;
typedef V<S> vs;
typedef long long ll;
typedef pair<int,int> pii;


S solve(S s) {
	if (s == "") return "";
	char big;
	ifor(i, 25, 0) {
		if (count(all(s), 'A'+i)) {
			big = 'A' + i;
			break;
		}
	} 
	S smaller = "";
	rep(i, si(s)) {
		if (s[i] != big) {
			smaller += s[i];
		} else {
			S ans = solve(smaller);
			fori(j, i, si(s)) {
				if (s[j] == big) ans = big + ans;
				else ans = ans + s[j];
			}
			return ans;
		}
	}
	return "";
}

int main() {
	int t = SS;
	rep(_, t) {
		S s;
		cin>>s;
		printf("Case #%d: ", _+1);
		cout<<solve(s);
		puts("");
	}
}


