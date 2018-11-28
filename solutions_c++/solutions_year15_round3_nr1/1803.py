#include<bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define se second
#define fi first


using namespace std;
typedef long long ll;
typedef pair < int, int > pii;
typedef pair < int , pii > tuple;
typedef vector < int > vi;
const int MAX = 205;
const int INF = 1e9+9;


int main(){
	
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int t;
	cin >> t;
	int r,c,w;
	int ans, a;
	int ntc = 1;
	while( t-- ){
		cin >> r >> c >> w;
		a = c/w - 1;
		ans = a + (int)ceil( (c-a*w)/(w*1.0) ) + w-1;
		printf("Case #%d: %d\n", ntc, ans );
		ntc++;
	}
	

	return 0;
}

