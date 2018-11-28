#include <bits/stdc++.h>

using namespace std;

/// DFNS
#define mp(x,y) make_pair(x,y)
#define ff first
#define ss second
#define pb(x) push_back(x)
#define fr(i,n) for (int i=1; i<=n; i++)
#define sz size
#define sqr(x) ((x)*(x))
#define all(x) x.begin(), x.end()
/// TPDFS
typedef unsigned long long ulld;
typedef long long lld;
typedef string str;
typedef pair<int,int> pii;

int t;
																		
int main (){
	
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	cin >> t;
	
	for (int i = 1; i <= t; i++){
		lld np = 0, n;
		str q;
		cin >> n >> q;
		lld sf = q[0] - '0';
		for (int j = 1; j <= n; j++){
			if (q[j] == '0')
				continue;
			if (sf < j)
				np += (j - sf), sf += np;
			sf += q[j] - '0';
		}
		cout << "Case #" << i << ": " << np << "\n";
	}
	
	return 0;
}
