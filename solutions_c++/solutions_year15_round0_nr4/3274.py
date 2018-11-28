#include<bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define se second
#define fi first

using namespace std;
typedef long long ll;
typedef pair < int, int > pii;
typedef vector < int > vi;
const int MAX=  1e5+5;


int main(){
	
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	
	int t;
	cin >> t;
	
	int x,r,c,id, ntc =1;
	string ans[2] = {"GABRIEL", "RICHARD"};

	
	while( t-- ){
		cin >> x >> r >> c;
		id = 0;
		if( r*c % x != 0 ) id = 1;
		else{
			if( r < x-1 || c < x-1 ) id = 1;
		}

		printf("Case #%d: %s\n", ntc, ans[id].c_str() );
		ntc ++;
	}
	
	return 0;
}
