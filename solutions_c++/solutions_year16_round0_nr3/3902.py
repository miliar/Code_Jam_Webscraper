#include<bits/stdc++.h>
#define endl '\n'
#define pb push_back
#define pii pair<int, int>
#define mp make_pair
#define ll long long
#define ld long double
using namespace std;

const int n = 16;
const int j = 50;
const ll MAX = 15*1e7;
bool isCmp[MAX+1];
ll divis[MAX+1];
vector<ll> primes;

void printBin(int i){
// 	cout << i << " -> ";
	vector<int> digits;
	while(i!=0){
		digits.pb(i%2);
		i /= 2;
	}
	for(int i=(int)digits.size()-1;i>=0;--i)
		cout << digits[i];
	cout << " ";
}

void getPrimes(){
	ll upper = (ll)sqrt((ld)MAX);
	memset(isCmp, false, sizeof(bool) * (MAX + 1));
	memset(divis, -1, sizeof(int)*(MAX + 1));
	isCmp[0] = true;
	isCmp[1] = true;
	for(ll m=2;m<=upper;++m)
		if(!isCmp[m])
			for (ll k=m*m;k<=MAX;k+=m){
				isCmp[k] = true;
				divis[k] = m;
			}
	for(ll i=2;i<=MAX;++i)
		if(!isCmp[i])
			primes.pb(i);
// 	cout << "Found " << primes.size() << " primes.\n";
}

ll base(int i, int b){
	int cur = 0;
	ll res = 0;
	while(i!=0){
		res += (ll)(i%2)*(ll)pow(b, cur);
		i /= 2;
		cur++;
	}
	return res;
}

vector<ll> bases(int i){
	vector<ll> res;
	for(int b=2;b<=10;++b)
		res.pb(base(i, b));
	return res;
}

bool checkPrime(ll i){
	if(i <= MAX)
		return !isCmp[i];
	else{
		for(int p : primes)
			if(p <= (ll)sqrt((ld)i))
				if(i%p == 0)
					return false;
	}
	return true;
}

ll getDiv(ll i){
	if(i <= MAX)
		return divis[i];
	else{
		for(int p : primes)
			if(p <= (ll)sqrt((ld)i))
				if(i%p == 0)
					return p;
	}
	return -1;
}

void f(){
	int count = 0;
	for(int i=(1<<(n-1))+1;i<=(1<<n)-1 && count < j;i+=2){
// 		cout << i << " -> ";
// 		for(ll x : bases(i)) cout << x << "(" << checkPrime(x) << ") "; cout << endl;
		vector<ll> lol = bases(i);
		bool ok = true;
		for(ll x : lol){
			if(checkPrime(x)){
				ok = false;
				break;
			}
		}
		if(ok){
			printBin(i);
			for(ll x : bases(i))
				cout << getDiv(x) << " ";
			cout << endl;
			count++;
		}
	}
}

int main(){
	ios_base::sync_with_stdio(0);
// 	int ncases, caseNumber = 1;
// 	cin >> ncases;
// 	while(ncases--){
	getPrimes();
	cout << "Case #1:\n";
	f();
// 	for(ll x : bases(35))
// 		cout << x << " ";
// 	cout << endl;
// 		cout << "Case #" << caseNumber << ": " << f(0) << endl;
// 		caseNumber++;
// 	}
	return 0;
}