#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <queue>
#include <string.h>
#include <set>

#define ll long long

using namespace std;

// string check(ll beg, ll &r, ll &p, ll &s, ll depth) {

// 	if(depth == 0){

// 		if()

// 		return string('R' + beg();
// 	}
	
// 	ll left = beg;

// 	if(beg == 0){
// 		ll right = 2;

// 	} else if(beg == 1) {
// 		ll right = 0;

// 	} else if(beg == 2){
// 		ll right = 1;

// 	}

// }

struct tri{
	ll a,b,c;
};

tri func[30][3];


string go(int n, int j){
	if(n == 0){
		// char c = 'P' + j;
		// return string(c);
		// string rr = "";
		// rr += c;
		// return rr;
		if(j == 0){
			return "P";
		}

		if(j == 1) return "R";
		if(j == 2) return "S";
		// return string('P' + j);
	}


	int left, right;

	if(j == 0){
				left = 0; right = 1;
			} else if(j == 1) {
				left = 1;
				right = 2;
			} else {
				left = 0;
				right = 2;
			}

	string s1 = go(n-1, left);
	string s2 =  go(n-1, right);
	if( s1 < s2)
		return s1 + s2;
	else return s2 + s1;
}

void solve(int t) {
	ll n;
	cin>>n;
	ll r,p,s;
	cin>>r>>p>>s;
	// cout<<"k\n";
	func[0][0].a = 1;
	func[0][1].b = 1;
	func[0][2].c = 1;

	for(int i=1; i<21; ++i)
		for(int j=0; j<3; ++j){

			int left, right;

			if(j == 0){
				left = 0; right = 1;
			} else if(j == 1) {
				left = 1;
				right = 2;
			} else {
				left = 0;
				right = 2;
			}

			func[i][j].a = func[i-1][left].a + func[i-1][right].a;
			func[i][j].b = func[i-1][left].b + func[i-1][right].b;
			func[i][j].c = func[i-1][left].c + func[i-1][right].c;

		}
		
	for(int j=0; j<3; ++j){
		if(func[n][j].a == p && func[n][j].b == r && func[n][j].c == s){
			// cout<<"Possible\n";
		cout<<"Case #"<<t<<": "<<go(n,j)<<"\n";

			return;
		} 

	}

	
	// for(int i=0; i<)

	cout<<"Case #"<<t<<": "<<"IMPOSSIBLE"<<"\n";

}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int T;
	cin>>T;
	int t = 1;
	while(T--)
		solve(t++);

	return 0;

}