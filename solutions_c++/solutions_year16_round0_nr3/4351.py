#include <bits/stdc++.h>
using namespace std;

#define ll long long int
#define mp(i,j) make_pair(i,j)
#define pb(x) push_back(x)
#define MOD 1000000007

const ll MAX = 8589934591;
const ll LMT = 92682;
 
ll _c[(MAX>>6)+1];
vector<ll> primes;
 
#define IsComp(n)  (_c[n>>6]&(1<<((n>>1)&31)))
#define SetComp(n) _c[n>>6]|=(1<<((n>>1)&31))
 
void prime_sieve() {
    for (ll i = 3; i <= LMT; i += 2)
        if (!IsComp(i))
            for (ll j = i*i; j <= MAX; j += i+i)
                SetComp(j);
 
    primes.push_back(2);
    for (ll i=3; i <= MAX; i += 2)
        if (!IsComp(i))
            primes.push_back(i);
}
 
bool is_prime(ll n) {
	if(n==2) return true;
    if ((n < 2) || (n%2 == 0)) return false;
    return !IsComp(n);
}

ll findnum(bitset <16> &b,ll base,ll n)
{
	ll j,num = 0;

	for(j=0;j<n;j++) {
		num = num + b[j]*pow(base,j);
	}
	return num;
}

ll pollardRho(ll N)
{
        if(N%2==0) return 2;
        ll x = rand()%(N-1) + 1;
        ll y = x;
	
        ll c = 1;
        ll g = 1;

        while(g==1) {         
                x = ((x*x)%N+c)%N;
                y = ((y*y)%N+c)%N;
                y = ((y*y)%N+c)%N;
                g = __gcd((ll)abs(x-y),N);
	}
        return g;
}

int main()
{
	bitset <16> bb;
	ll c,t,n,i,j,jj,smallest,largest,d,flag,cnt,sz,szz;
	ll num[11];
	vector <pair<bitset<16> , vector<ll> > > ans;
	vector <ll> div;

	scanf("%lld", &t);

	for(c=1;c<=t;c++) {
		scanf("%lld%lld", &n,&jj);

		largest = pow(2,n)-1;
		smallest = 1 + pow(2,n-1);

//		cout<<largest<<" "<<smallest<<endl;

		cnt = 0;

		for(i=smallest;i<=largest;i++) {
			if(i%2==0) continue;
			bb = i;
			flag = 0;

		//	cout<<"checking: "<<bb<<endl;

			for(j=2;j<=10;j++) {
				num[j] = findnum(bb,j,n);
		//		cout<<"In base :"<<j<<" number is: "<<num[j]<<endl;
			}

			div.clear();

			for(j=2;j<=10;j++) {
				d = pollardRho(num[j]);

		//		cout<<"divisor of: "<<num[j]<<" is: "<<d<<endl;

				if((d==1) || (d==num[j])) {
					flag = 1;
					break;
				} else {
					div.pb(d);
				}
			}

			if(flag==0) {
				ans.pb(mp(bb,div));
				cnt++;
				if(cnt==jj) break;
			}
		}
		sz = ans.size();

		cout<<"Case #"<<c<<":"<<endl;
		for(i=0;i<sz;i++) {
			div = ans[i].second;
			szz = div.size();
			
			cout<<ans[i].first<<" ";
			for(j=0;j<szz;j++) {
				cout<<div[j]<<" ";
			}
			cout<<endl;
		}

		ans.clear();
	}

	return 0;
}
