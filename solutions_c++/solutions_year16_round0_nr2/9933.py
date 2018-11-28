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
#define MAX 100
#define MOD 1000000007
#define endl "\n"
#define after_dec(a) cout<<fixed<<setprecision((a))
//#define TIMER cout<<endl<<"Time Taken : "<<(double)(clock()-t1)/CLOCKS_PER_SEC<<" seconds."<<endl
#define FILE freopen("B-large.in", "r", stdin); freopen("B-large.out", "w", stdout)
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

char S[MAX+5];

bool checker(){
	ll i = 0;
	bool flag = true;
	while(S[i]!='\0'){
		if(S[i++] == '-'){
			flag = false;
			break;
		}
	}
	return flag;
}

void flip(ll pos){
	char temp[MAX+5];
	ll i = 0;
	rep(i, 0, pos){
		if(S[pos-i] == '-') temp[i] = '+';
		else temp[i] = '-';
		//temp[i] = S[pos-i];
	}
	while(S[i]!='\0'){
		temp[i] = S[i];
		i++;
	}
	ll j = 0;
	rep(j,0,i-1){
		S[j] = temp[j];
	}
}

int main(){
	FAST;
	#ifdef FILE
		FILE;
	#endif
	ll t, n, i, j, k;
	cin>>t;
	rep(i, 1, t){
		k = 0;
		cin>>S;
		while(!checker()){
			if(S[1] == '\0'){
				flip(0);
			}else{
				j = 1;
				while(S[j]!='\0' && S[j]==S[j-1]){
					j++;
				}	
				flip(j-1);
			}
			k++;
		}
		cout << "Case #"<<i<<": "<<k<<endl;
	}
	#ifdef TIMER
		TIMER;
	#endif
	return 0;
}
