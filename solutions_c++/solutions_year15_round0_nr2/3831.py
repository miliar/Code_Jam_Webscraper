#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;

#define pb push_back
#define pp pop_back
#define f first
#define s second
#define mp make_pair
#define sz(a) int((a).size())
#define fname "."

const int N = (int)1e5 + 123;
const double eps = 1e-6;
const int inf = (int)1e9 + 123;

using namespace std;

int t;
int n;
vector < int > a;
map < vector < int >, int > d;

int D(vector < int > a) {
    if (d.count(a))
    	return d[a];
    int mini = a.back();
    vector < int > nw;
    for (int i = 0; i < sz(a); i++)
    	if (a[i] > 1)
    		nw.pb(a[i] - 1);
	if (!nw.empty())
		mini = min(mini, D(nw) + 1);
	for (int i = 0; i < sz(a); i++) {
	    if (a[i] == 1)
	    	continue;
		for (int j = 1; j < a[i]; j++) {
			nw = a;	
			nw.erase(nw.begin() + i);		
			nw.pb(j);
			nw.pb(a[i] - j);
			sort(nw.begin(), nw.end());
			mini = min(mini, D(nw) + 1);
		}
	}
	return d[a] = mini;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin >> t;
	for (int test = 1; test <= t; test++) {
		cin >> n;
		a.resize(n);
		for (int i = 0; i < n; i++)
			cin >> a[i];
		sort(a.begin(), a.end());
		int ans = D(a);
//		cout << ans << " ";
		cout << "Case #" << test << ": " << ans << endl;
	}
	return 0;
}
