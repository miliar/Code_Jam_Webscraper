/* sidchelseafan */
#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define mp make_pair
#define sz(a) (int)a.size()
#define pii pair<int,int>
#define pll pair<ll,ll>

//Hardware Instructions
#define bitcount __builtin_popcount
#define gcd __gcd

//Trasersal Macros
#define rep(i,n) for(int i=0, _##i=(n); i<_##i; ++i)
#define dwn(i,n) for(int i=(n); --i>=0; )
#define repr(i,l,r) for(int i=(l), _##i=(r); i<_##i; ++i)
#define dwnr(i,l,r) for(int i=(r), _##i=(l); --i>=_##i; )
#define repi(i,a) for(__typeof((a).begin()) i=(a).begin(), _##i=(a).end(); i!=_##i; ++i)
#define dwni(i,a) for(__typeof((a).rbegin()) i=(a).rbegin(), _##i=(a).rend(); i!=_##i; ++i)
#define all(a) a.begin(),a.end()
#define fill(a,s) memset(a,s,sizeof(a));
#define ff first
#define ss second
#define abs(x) (x<0?(-x):x)

using namespace std;
const ll MX=100000;
const ll MOD = 1000000007;
ll fast_exp(ll base,ll exp,ll mod){
  ll res=1;
  while(exp > 0){
    if (exp%2==1)res=(res*base)%mod;
    base = (base*base)%mod;
    exp/=2;
   }
  return res;
}
ll modulo(ll a,ll b,ll c){
    long long x=1,y=a; // long long is taken to avoid overflow of intermediate results
    while(b > 0){
        if(b%2 == 1){
            x=(x*y)%c;
        }
        y = (y*y)%c; // squaring the base
        b /= 2;
    }
    return x%c;
}
/* Miller-Rabin primality test, iteration signifies the accuracy of the test */
/* this function calculates (a*b)%c taking into account that a*b might overflow */
long long mulmod(long long a,long long b,long long c){
    long long x = 0,y=a%c;
    while(b > 0){
        if(b%2 == 1){
            x = (x+y)%c;
        }
        y = (y*2)%c;
        b /= 2;
    }
    return x%c;
}
bool Miller(long long p,int iteration){
    if(p<2){
        return false;
    }
    if(p!=2 && p%2==0){
        return false;
    }
    long long s=p-1;
    while(s%2==0){
        s/=2;
    }
    for(int i=0;i<iteration;i++){
        long long a=rand()%(p-1)+1,temp=s;
        long long mod=modulo(a,temp,p);
        while(temp!=p-1 && mod!=1 && mod!=p-1){
            mod=mulmod(mod,mod,p);
            temp *= 2;
        }
        if(mod!=p-1 && temp%2==0){
            return false;
        }
    }
    return true;
}
ll arr[111][111];
int check[111111];
void Pre(){
	for (int i=2; i <= 10; i++){
		arr[i][0] = 1;
		for (int j=1; j <= 16; j++)
			arr[i][j] = i*arr[i][j-1];
	}
}
//Calculate string s in base "base" , answer in base10
ll calc(string s, int base){
	ll ans = 0;
	int n = sz(s);
	rep(i, n){
		ans += (s[i] - '0')*(arr[base][n - i - 1]);
	}
	return ans;
}
vector<string> store[111];
int main(){

	ll LIM = 111111;
	Pre();
	
	for (ll i=2; i*i < LIM ; i++){
		if (!check[i]){
			for (ll j = 2*i; j < LIM; j += i){
				check[i] = 1;
			}
		}
	}

	int len = 16;
	for (ll num = 1; num < (1<<len); num++ ){
		string tmp;
		for (int i=0; i < len; i++){
			if (num & (1<<i)) tmp += '1';
			else tmp += '0';
		}

		/*int idx = sz(tmp);
		rep(i, sz(tmp)){
			if (tmp[i]=='0') idx=i;
			else break;
		}

		if (idx!=sz(tmp)) tmp=tmp.substr(idx+1);*/
		tmp.erase(0, tmp.find_first_not_of('0'));
		if (tmp[sz(tmp) - 1] == '1'){
			bool all = true;
			for (int i=2; i <= 10; i++){
				ll num = calc(tmp, i);
				all = (all && !Miller(num, 20));
			}
			if (all) 
				store[sz(tmp)].pb(tmp);
		}
	}
	
	cout << sz(store[16]) <<"size\n";

	vector< string > make;
	//set < string > make_s;
	for(int i=0; i < 1000; i++){
		make.pb(store[len][i]);
		//make_s.insert(store[len][i]);
	}
	//cout << make_s.size() << " " << make.size()<<" size\n";
	vector < pair< string, vector<int> > > make_divi;
	sort(all(make));
	rep(i, 1000){
		vector<int> in;
		for (int j=2; j <= 10; j++){
			ll num = calc(make[i], j);
			for (int k=2;k<=100;k++){
				if (num%k==0){
					in.pb(k);
					break;
				}
			}
		}
		if (sz(in) == 9)
			make_divi.pb(mp(make[i], in)); 
	}

	int n, j;
	cin >> n >> j;
	
	if (n == 16){
		freopen("16.in", "w", stdout);
		cout <<"Case #1:\n";
		rep(i, 50){
			cout << make_divi[i].ff <<" ";
			vector<int> index = make_divi[i].ss;
			rep(j, sz(index))
				cout << index[j]<<" ";
			cout << "\n";
		}
	}
	else{
		freopen("32.in", "w", stdout);
		cout <<"Case #1:\n";
		string tmp;
		rep(i, 16) tmp += '0';
		rep(i, 500){
			cout << make_divi[i].ff+tmp <<" ";
			vector<int> index = make_divi[i].ss;
			rep(j, sz(index))
				cout << index[j]<<" ";
			cout << "\n";
		}
	}


	
	return 0;
}