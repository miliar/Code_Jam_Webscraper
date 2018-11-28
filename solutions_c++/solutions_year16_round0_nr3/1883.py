#include <iostream>
#include <set>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

typedef  long long ll;

#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)

ll gcd(ll a, ll b){
	if(b == 0)return abs(a);
	return gcd(b, a % b);
}
ll mul_mod(ll a, ll b, ll m){
	// determine largest bit which is set in b
	int largestBit = 0;
	while((b >> largestBit) != 0){
		largestBit++;
	}
	
	// multiplication
	ll result = 0;
	for(int currentBit = largestBit - 1; currentBit >= 0; currentBit--){
		result = (result + result); // result *= 2;

		if(result >= m)result -= m; // result %= m;

		if((b >> currentBit) & 1){ // check whether current bit is set in b
			result += a;
			if(result >= m)result -= m; // result %= m;
		}
	}
	return result;
}

ll exp_mod(ll a, ll x, ll m) {
    if (x == 0) return 1;
    ll res = exp_mod(a, x/2, m);
    res = mul_mod(res, res, m); //(res * res) % m;
    if(x % 2 == 1) res = mul_mod(res, a, m); // (res * a) % m
    return res;
}

ll random(ll a, ll b) {
    ll intervallLength = b - a + 1;
	ll todo = intervallLength;
    ll base = RAND_MAX;
    ll result = 0;
    for(ll todo = intervallLength; todo > 0; todo /= base){
        result = mul_mod(result, base, intervallLength);
		result = (result + rand()) % intervallLength;
    }
    if(result < 0) result += intervallLength;
    return result + a; 
}

bool witness(ll a, ll n) {
	ll u = n-1;
    int t = 0;
    while (u % 2 == 0) {
        t++;
        u /= 2;
    }
    ll next = exp_mod(a, u, n);
    if(next == 1)return false;
    ll last;
    for(int i = 0; i < t; i++) {
    	last = next;
        next = mul_mod(last, last, n);//(last * last) % n;
        if (next == 1){
        	return last != n - 1;
        }
    }
    return next != 1;
}
 
// Miller-Rabin-Test, s = # iterations
// probability for an error <= 2^(-s)
bool millerRabin(ll n, int s) {
    if (n <= 1) return false;
    if (n == 2) return true;
    if (n % 2 == 0) return false;
    for(int i = 0; i < s; i++) {
        ll a = random(1, n-1);
        if (witness(a, n)) {
			return false;
		}
    }
    return true;
}

// uses Miller-Rabin
bool isPrime(ll val){
	return millerRabin(val, 20);
}

ll rho(ll n) {
	ll x, y, i = 1, k = 2, d;
	x = y = random(0,n-1);
	while(1) {
		++i;
		x = (mul_mod(x,x,n));
		x += 2;
		if(x >= n) x-= n;
		if(x == y) return 1;
		d = gcd(abs(x-y),n);
		if(d != 1) return d;
		if(i == k) {
			y=x;
			k*=2;
		}
	}
	return 1;
}

vector<ll> factors(ll n){
	vector<ll> res;
	if(n == 1)return res;
	if(isPrime(n)){
		res.push_back(n);
	} else {
		ll d = 1;
		while(d == 1)d = rho(n);
		vector<ll> dd = factors(d);
		res = factors(n / d);
		FORIT(it, dd)res.push_back(*it);
	}
	return res;
}

int calc(ll val){
	vector<ll> f = factors(val);
	return f.size();
}
vector<long long> calc2(ll val){
	vector<ll> f = factors(val);
	return f;
}
long long conver(string &s,int base){
	long long ans=0;
	long long exp=1LL;
	for(int i=s.size()-1;i>=0;i--){
		if(s[i]=='1')ans+=exp;
		exp*=base;
	}
	return ans;
}
int n,j;
set<string>st,ya;
int main() {
	//ios::sync_with_stdio(false);cin.tie(0);
    int cases;
    cin>>cases;
    int tc=1;
    while(cases--){
		cout<<"Case #"<<tc++<<":\n";
		cin>>n>>j;
		for(int valid=0;valid<j;){
			int unos=rand()%n;
			string s(unos,'1');
			for(int i=unos;i<n;i++)s+="0";
			random_shuffle(s.begin(),s.end());
			s[0]=s[s.size()-1]='1';
			if(ya.count(s))continue;
			ya.insert(s);
			bool check=true;
			for(int base=2;base<=10;base++){
				long long number=conver(s,base);
				if(calc(number)==1){check=false;break;}
			}
			if(check){st.insert(s),valid++;}
		}
		for(string s:st){
			//if(print)cout<<"X";
			bool print=false;
			print=true;
			cout<<s;
			for(int base=2;base<=10;base++){
				long long number=conver(s,base);
				vector<long long>ans=calc2(number);
				cout<<" "<<ans[0];
			}
			cout<<"\n";
		}
    }
 }


