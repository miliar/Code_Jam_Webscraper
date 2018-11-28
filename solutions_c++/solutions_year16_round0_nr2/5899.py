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
        if (ex&1)r=(r * b)%mod;
        ex = ex >> 1;
        b = (b * b)%mod;}
    return r;
}

ll n,t;

int main(){
	// #ifndef USE_ONLINE_JUDGE 
	//    freopen("input.txt", "r", stdin);
	//    freopen("output.txt", "w", stdout);
	// #endif
    ios_base::sync_with_stdio(0);

    cin >> t;
    for (int testcase = 1; testcase <=t; ++testcase)
    {
    	string s;
    	cin >> s;
    	int l =s.length();
    	int ans=0;
    	for (int i = 1; i <l ; ++i)
    	{
    		if(s[i]!=s[i-1]){
    			ans++;
    		}
    	}
    	if(s[l-1]=='-')ans++;
    	cout << "Case #" << testcase << ": "<< ans <<"\n" ;
    }
    return 0;
}