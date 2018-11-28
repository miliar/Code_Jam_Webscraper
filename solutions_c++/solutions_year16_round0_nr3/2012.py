#include<bits/stdc++.h>
using namespace std;
#define endll           "\n"
#define INIT(n,m)       memset(n,m,sizeof(n))
#define REP(i,n)        for(ll i=0;i<n;i++)
#define FOR(i,a,b)      for(ll i=a;i<=b;i++)
#define FORD(i,a,b)     for(ll i=a;i>=b;i--)
#define PB              push_back
#define IN(a,b)         substr(a,b-a+1)
#define FF              first
#define SS              second
#define LEN(x)          ((ll)x.size())
#define MM              1000000007
#define CHECK(x,y)      (((x%=y)+=y)%=y)
#define DEBUG(x)        {cout<<#x<<" = ";cout << (x) << endll;}
#define PR(v)           {cout<<#v<<" = ";for(auto _:v)cout<<_<<' ';cout<<endll;}
#define PRR(a,b,n)      {cout<<#a<<" = ";FOR(_,b,n)cout<<a[_]<<' ';cout<<endll;} 
#define FOREACH(it, c)  for(__typeof((c).begin())it=(c).begin();it!=(c).end();++it)
#define FILE_IO(a,b)    {freopen(a,"r",stdin);freopen(b,"w",stdout);}
struct  IO              {IO(){ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);}}_;
typedef long long ll;
typedef pair<ll,ll> ii;
ll n,m,len,k,t,a,b;

bool isPrime[33333335];
ll divisor[33333335];
vector<ll> primes;

void sieve(){
	INIT(isPrime,true);
	isPrime[0] = isPrime[1] = false;
	
	for(ll i=2;i<=33333334;i++) if(isPrime[i]){
		for(ll j=i*i;j <= 33333334; j+= i){
			isPrime[j] = false;
			divisor[j] = i;
		}
		primes.PB(i);
		divisor[i] = i;
	}
}

ll conv(ll x, ll b){
	ll ret = 0;
	ll temp = 1;
	
	while(x){
		ret += temp * (x%10);
		temp *= b;
		
		x /= 10;
	}
	return ret;
}

ll divs(ll x){
	if(x <= 33333334) return divisor[x];
	for(auto cur:primes){
		if(x % cur == 0) return cur;
	}
	return x;
}

int main(){
	FILE_IO("C-small-attempt0.in","output.txt");
	cin >> t >> a >> b;
	cout << "Case #1:\n";
	INIT(divisor,-1);
	sieve();
	
	ll cnt = 0;
	
	REP(i,1LL<<13){
		
		ll j = 0;
		FORD(k,12,0){
			j *= 10;
			if(i & (1LL<<k)) j++;
		}
		
		ll now = 1000000000000001 + j*10;
		
		bool fnd = false;
		
		vector<ii> v;
		
		FOR(b,2,10){
			ll nx = conv(now,b);
			ll div = divs(nx);
			v.PB(ii(nx,div));
			if(div == nx) fnd = true;
		}
		if(!fnd){
			cout << now;
			for(auto cur:v){
				cout << " " << cur.SS;
			}
			cout << endll;
			cnt++;
			if(cnt >= 50){
				return 0;
			}
		}
		
	}
	return 0;
}
