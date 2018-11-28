#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <set>

#define pb push_back
#define mp make_pair
#define ll long long
#define forn(i, n) for (int i = 0; i < (int) n; i++)

const int INF = 1e9;

using namespace std;


int main()
{
    freopen("a.in", "rt", stdin);
    freopen("a.out", "wt", stdout);

    int t, n;

    scanf("%d", &t);

    string s;

    forn(t1, t) {
    	cin >> n >> s;
    	int res = 0, cur = 0;

    	forn(i, s.length()) {
    		res = max(res, i - cur);
    		cur += (s[i] - '0');
    	}
    	cout << "Case #" << t1 + 1 << ": " << res << endl;
    }


    return 0;
}