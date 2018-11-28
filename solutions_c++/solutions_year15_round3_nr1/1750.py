#include <iostream>
#include <cstdio>
#include <string>
#include <utility> // pair
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstring> //memset
using namespace std;
  
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii; 
typedef long long ll;
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 
#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) 
#define rep(i,n) for (i=0; i<n ; i++)
#define rep1(i,n) for (i=1; i<=n ; i++)
#define MOD 1000000007
#define MAX 1000005
ll a[MAX];

int main () {

	freopen ("in.txt", "r", stdin);
	freopen ("out.txt", "w", stdout);
	ll t, i, z, r, c, w, res;
	cin >> t;
	rep1(z, t) {
		cin >> r >> c >> w;
		if(w==c) res = w;
		else res = (ceil((float)c/w) -1 + w);

		printf("Case #%lld: %lld\n", z, res);
	}

	return 0;
}