#include <bits/stdc++.h>
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define RFOR(i,a,b) for(int i=(b) - 1;i>=(a);i--)
#define REP(i,n) for(int i=0;i<(n);i++)
#define RREP(i,n) for(int i=n-1;i>=0;i--)

#define PB push_back
#define MP make_pair
#define ALL(a) (a).begin(),(a).end()
#define RALL(a) (a).rbegin(),(a).rend()
#define CLR(a) memset(a,0,sizeof(a))
#define SET(a,c) memset(a,c,sizeof(a))

#define DEBUG(x) cout<<"#x"<<": "<<x<<endl

using namespace std;

typedef long long int ll;
typedef vector<int> vi;
typedef vector<ll> vl;

const ll INF = INT_MAX/3;
const ll MOD = 1000000007;
const double EPS = 1e-14;
const int dx[] = {1,0,-1,0} , dy[] = {0,1,0,-1};

int intri(ll n){
    for(ll i=2;i*i<=n;i++){
	if( n % i == 0) return i;
    }
    return -1;
}

bool primes[1000000];

string toBin(ll n){
    string ret;
    while(n > 0){
	ret = char( (n&1) + '0') + ret;
	n >>= 1;
    }
    return ret;
}
int main(){
    int t;
    cin >> t;
    REP(a,t){
	printf("Case #%d:\n",a+1);
	ll n,j;
	cin >> n >> j;
	REP(i,1<<(n-2)){
	    if(j == 0) break;
	    ll tn = ll(i)*2 + (1<<(n-1)) + 1;
	    vector<ll> num(11,0);
	    num[2] = tn;
	    FOR(k,3,11){
		ll temp = tn;
		ll p = 1;
		while(temp > 0){
		    num[k] += (temp&1) * p;
		    temp >>= 1;
		    p *= k;
		}
	    }
	    bool flg = true;
	    FOR(k,2,11){
		num[k] = intri(num[k]);
		if(num[k] == -1){
		    flg = false;
		    break;
		}
	    }

	    if(flg){
		cout << toBin(tn);
		FOR(k,2,11){
		    cout << " " << num[k];
		}
		cout << endl;
		j--;
	    }
	}
    }

    return 0;
}


