#include <bits/stdc++.h>
using namespace std;

#define MEM(arr,val)memset((arr),(val), sizeof (arr))
#define PI (acos(0)*2.0)
#define FASTER ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

ll gcd(ll a,ll b){return b == 0 ? a : gcd(b,a%b);}
ll lcm(ll a,ll b){return a*(b/gcd(a,b));}

/**
 * __builtin_popcount(int d) // count bits
 * __builtin_popcountll(long long d)
 * strtol(s, &end, base); // convert base number
 */
//----------------------------------------------------------------------//

int main(){
	FASTER;
	int T,Case=1;
	cin >> T;
	while(T--){
		string s;
		cin >> s;
		reverse(s.begin(), s.end());

		int i = 0;
		int c = 0;
		while(i < s.size() && s[i] != '-'){
			if(s[i++] == '-'){
				c = 1;
				break;
			}
		}
		while(i<s.size()){
			if(	s[i] != s[i-1])c++;
			i++;
		}

		cout << "Case #" << (Case++)  <<": " << c << endl;
	}

	return 0;
}
