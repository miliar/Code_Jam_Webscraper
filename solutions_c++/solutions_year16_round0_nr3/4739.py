#include <bits/stdc++.h>


#define mp make_pair
#define pb push_back
#define F first
#define S second
#define N 100010
#define dbg(x) {cerr << #x << " = " << x << endl;}
#define dbg2(x,y) {cerr << #x << "," << #y << " = " << x << " " << y << endl;}
#define dbg3(x,y,z) {cerr << #x << "," << #y << "," << #z << " = " << x << " " << y << " " << z << endl;}
typedef long long ll;
typedef unsigned long long ull;
typedef double dbl;
using namespace std;
ll mod = 1000000007;

inline ll mpow(ll b, ll ex){
	if (b==1)return 1;
    ll r = 1;
    while (ex ){
        if (ex&1)r=(r * b);
        ex = ex >> 1;
        b = (b * b);}
    return r;
}

ll n,t,j;

ll factor(ll n){
	for (ll i = 2; i*i <= n; ++i)
	{
		if (n%i==0)return i;
	}
	return 0;
}

ll eval(ll num,ll base){
	if (num>0)return (num&1) + eval(num/2,base)*base;
	return 0;
}

void print(ll num){
	if (num==0) return;
	print(num/2);
	cout <<  ((num&1)?"1":"0") ;
}

int main(){
	// #ifndef USE_ONLINE_JUDGE 
	//    freopen("input.txt", "r", stdin);
	//    freopen("output.txt", "w", stdout);
	// #endif
    ios_base::sync_with_stdio(0);

    cin >> t;
    for (int testcase = 1; testcase <=t; ++testcase)
    {
    	cin >> n >> j;
    	ll f=0,i=0;
    	std::vector< std::vector<ll> > ans;
    	std::vector< ll > res;
    	while(f<j and i<(1L<<ll(n))/2 ){
    		ll num = (1L<<ll(n-1))+1+ll(i<<1),base;
    		std::vector< ll> v(9,0);
    		for (base = 2; base < 11; ++base)
    		{
    			ll val = eval(num,base);
    			ll divisor=factor(val);
    			if (divisor==0)break;
    			v[base-2]=divisor;
    		}
    		if (base==11)
    		{
    			res.push_back(num);
    			ans.push_back(v);
    			f++;
    		}
    		cerr << i << endl;;
    		i++;
    	}


    	cout << "Case #" << testcase << ":\n" ;
    	for (ll k = 0; k < j; ++k)
    	{
    		print(res[k]);
    		for (int i = 0; i < 9; ++i)
    		{
    			cout << " "<<  ans[k][i] ;	
    		}
    		cout << endl;
    	}
    }
    return 0;
}