#include <bits/stdc++.h>
using namespace std;
#define FAST ios::sync_with_stdio(false)
#define mp make_pair
#define mt make_tuple
#define pb push_back
#define fi first
#define se second
#define sz(x) ((int) (x).size())
#define a_size(x) sizeof(x)/sizeof(x[0])
#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x) * (x))
#define sqrt(x) sqrt(abs(x))
#define fill(x,y) memset(x,y,sizeof(x))
#define rep(i, begin, end) for(i = (begin); i != (end) + 1 - 2 * ((begin) > (end)); i += 1 - 2 * ((begin) > (end)))
#define rep_stl(i, ob) for(auto i = ob.begin(); i != ob.end(); i++)
#define MAX 1000000
#define MOD 1000000007
#define endl "\n"
#define after_dec(a) cout<<fixed<<setprecision((a))
//#define TIMER cout<<endl<<"Time Taken : "<<(double)(clock()-t1)/CLOCKS_PER_SEC<<" seconds."<<endl
#define FILE freopen("A-small-attempt0.in", "r", stdin); freopen("A-small-attempt0.out", "w", stdout)
typedef long long ll;
typedef long double ld;
typedef double D;
typedef vector<int> vi;
typedef vector<long> vl;
typedef vector<ll> vll;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<vi> matrix;
typedef vector<vi> vii;
clock_t t1 = clock();

bool a[10];

void marker(ll num){
	ll ldig;
	while(num > 0){
		ldig = num%10;
		if(!a[ldig]){
			a[ldig] = 1;
		}
		num /= 10;
	}
}

bool checker(){
	bool flag = true;
	ll i = 0;
	rep(i, 0, 9){
		if(!a[i]){
			flag = false;
		}
	}
	return flag;
}

int main(){
	FAST;
	#ifdef FILE
		FILE;
	#endif
	ll i, t, n, last;
	i = 1;
	cin>>t;
	while(i <= t){
		fill(a,0);
		cin>>n;
		ll newNum = n;
		if(n==0){
			cout << "Case #"<<i<<": "<<"INSOMNIA"<<endl;
		}else{
			ll j = 1;
			while(!checker()){
				newNum = j*n;
				marker(newNum);
				j++;
			}
			cout << "Case #"<<i<<": "<<newNum<<endl;
		}
		i++;
	}
	
	#ifdef TIMER
		TIMER;
	#endif
	return 0;
}
