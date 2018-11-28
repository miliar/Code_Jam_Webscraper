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
#define MAX 111111
#define MOD 10000000007
ll a[MAX];

int main () {

	freopen ("a.in", "r", stdin);
	freopen ("a.out", "w", stdout);
	int t, i, z, s_max, ctr, extra;
	string str;
	cin >> t;
	z = 1;
	while(t--) {
		cin >> s_max;
		cin >> str;
		ctr = extra = 0;	
		ctr += (str[0]-'0');
		for(i=1 ; i<= s_max ; i++) {
			if (ctr >= i) {
				ctr += str[i]-'0';
			}
			else {
				extra += 1;
				ctr += 1;
				ctr += str[i]-'0';
			}
		}
		cout << "Case #" << z++ << ": " << extra << "\n";
	}
	return 0;
}