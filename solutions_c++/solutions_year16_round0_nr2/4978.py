#include <cstring>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <iostream>
#include <ctime>
#include <vector>
#include <map>
#include <set>

using namespace std;

#define pb push_back
#define sz(a) (int)a.size()
#define fs first
#define sc second

typedef long long ll;
typedef pair<int,int> ii;

int solve() {
    string s;
    cin >> s; int n = sz(s);
    string s2 = "";
    for (int i = 0; i < n; ++i)
        if (i==0 || s[i]!=s[i-1]) s2.pb(s[i]);
    int m = sz(s2);
    if (m==0) return 0;
    return m - (s2[m-1]=='+');
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t, tmp; cin >> t; tmp = t;
	while (t--)
        printf("Case #%d: %d\n",tmp-t,solve());
	return 0;
}
