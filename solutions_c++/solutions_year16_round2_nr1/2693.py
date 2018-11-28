#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define ld long double
#define inf 1000000000
#define eps 1e-9
#define all(a)   a.begin(),a.end()
#define mp make_pair
#define ff first
#define ss second
#define pb push_back
#define sz size()
#define mod 1000000007
#define sl(inp) scanf("%lld",&inp)
#define sd(inp) scanf("%d",&inp)
#define rep(i, a, b) for(int i = a; i < b ; ++i)
#define maxn 1000101

ll fpow(ll base,ll power){
	ll result = 1;
    while (power > 0){
    	if (power%2 == 1){
    		result=(result*base);
    	}
    	base = (base*base);
    	power/=2;
    }
	return result;
}

string str;
map<ll, string> mpp;

inline void pre(){
    mpp[0] = "ZERO";
    mpp[1] = "ONE";
    mpp[2] = "TWO";
    mpp[3] = "THREE";
    mpp[4] = "FOUR";
    mpp[5] = "FIVE";
    mpp[6] = "SIX";
    mpp[7] = "SEVEN";
    mpp[8] = "EIGHT";
    mpp[9] = "NINE";
}

bool check(char ch, ll intt){
    ll iy = 0;
    for ( iy = 0 ; iy < str.sz ; iy ++ ){
        if ( str[iy] == ch ){
            return 1;
        }
    }
    return 0;
}

void fch(ll intt){
    if(1){
        string temp = mpp[intt];
        ll iy = 0, ix = 0;
        for ( ix = 0 ; ix < temp.sz ; ix ++ ){
            for ( iy = 0 ; iy < str.sz ; iy ++ ){
                if(str[iy] == temp[ix]){
                    str.erase( str.begin() + iy );
                    goto there;
                }
            }
            there:;
        }
    }
}

int main(){
    pre();
    ll n;
    cin >> n;
    ll i;
    for ( i = 1 ; i <= n ; i ++ ){
        cin >> str;
        printf("Case #%lld: ", i);
        vector<ll> v;
        v.clear();
        while(check('Z', 0)){
            v.pb(0);
            fch(0);
        }
        while(check('W', 2)){
            v.pb(2);
            fch(2);
        }
        while(check('U', 4)){
            v.pb(4);
            fch(4);
        }
        while(check('X', 6)){
            v.pb(6);
            fch(6);
        }
        while(check('G', 8)){
            v.pb(8);
            fch(8);
        }
        while(check('O', 1)){
            v.pb(1);
            fch(1);
        }
        // cout << str << endl;
        while(check('T', 3)){
            v.pb(3);
            fch(3);
        }
        // cout << str << endl;
        while(check('F', 5)){
            v.pb(5);
            fch(5);
        }
        // cout << str << endl;
        while(check('S', 7)){
            v.pb(7);
            fch(7);
        }
        // cout << str << endl;
        ll atLast = str.sz ;
        for ( ll ind = 0 ; ind < atLast/4 ; ind ++ ){
            v.pb(9);
        }
        sort(all(v));
        for ( ll ind = 0 ; ind < v.sz ; ind ++ ){
            cout << v[ind] ;
        }
        cout << "\n";
    }
    return 0;
}
