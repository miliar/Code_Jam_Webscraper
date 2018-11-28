#include <bits/stdc++.h>
using namespace std;
const int dx[]={1,0,-1,0,1,-1,-1,1};
const int dy[]={0,1,0,-1,1,1,-1,-1};
const int INF = 1<<30;
const long long LINF = 1e18;
const int EPS = 1e-8;
#define PB push_back
#define mk make_pair
#define fr first
#define sc second
#define ll long long
#define reps(i,j,k) for(int i = (j); i < (k); i++)
#define rep(i,j) reps(i,0,j)
#define MOD 1000000007
typedef pair<int,int> Pii;
typedef pair<int, ll> Pil;
typedef vector<int> vi;
typedef vector<vi> vvi;
bool is_prime(ll n){
	for(ll i = 2; i*i <= n; ++i){
		if(n % i == 0)return false;
	}
	return n != 1;
}
ll llpow(int m,ll j){
	ll res = 1;
	rep(i,j){
		res *= m;
	}
	return res;
}
ll Change_NBase_To_MBase(string num,int m){
	int len = num.size();
	reverse(num.begin(),num.end());
	ll c = 0;
	rep(i,len){
		if(num[i] == '1'){
			c += llpow(m,i);
		}
	}	
	return c;
}
vector < ll > ok;
bool check(string s){
	ok.clear();
	if(s[0] == '0' || s[s.size()-1] == '0'){
		return false;
	}
	reps(i,2,11){
		ll res = Change_NBase_To_MBase(s,i);
	//	cout << res << "\n";
		if(is_prime(res)){
			return false;
		}
		for(ll j = 2; j*j <= res; ++j){
			while(res % j == 0){
				ok.PB(j);
				goto end;
			}
		}
		end:;
	}
	
	return true;
}
int main(){
	int T;
	//cin >> T;
	int N,J;
	//cin >> N >> J;
	N = 16;
	J = 50;
	puts("Case #1:");
	ll S = 1LL << N;
	for(ll i = 0; i < S; ++i){
		string s = "";
		if(J == 0){
			break;
		}
		for(ll j = 0; j < N; ++j){
			if((i>>j)&1){
				s += "1";
			}
			else{
				s += "0";
			}
		}
		if(check(s)){
			cout << s;
			rep(j,ok.size()){
				cout << " " << ok[j];
			}
			puts("");
			--J;
		}
		//cout << s << "\n";
	}
//	check("1001");
	return 0;
}