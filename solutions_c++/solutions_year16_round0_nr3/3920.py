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
    	power/= 2;
    }
	return result;
}

ll calc(string temp, ll base){
    ll xx, res = 0;
    for ( xx = temp.sz - 1 ; xx >= 0 ; xx -- ){
        res += (temp[xx] - '0') * fpow(base, temp.sz-1-xx);
    }
    return res;
}

ll toSend = -1, theNum;

bool isNotPrime(ll A){
    ll idx = 2;
    for ( idx = 2 ; idx <= sqrt(A) ; idx ++ ){
        if ( A % idx == 0 ){
            toSend = idx;
            return 1;
        }
    }
    return 0;
}

int main(){
    ll t, in = 1;
    sl(t);
    while(t--){
        printf("Case #%lld:\n", in++);
        ll N, J; sl(N); sl(J);
        string so = "1", se = "1";
        ll tobe = N - 2, i, j;
        // i -> 0's and j -> 1's
        for ( i = 0 ; i <= tobe ; i ++ ){
            j = tobe - i;
            string mains = "";
            ll ii = i, jj = j;
            
            while(jj -- ){
                mains.append("0");
            }
            while(ii -- ){
                mains.append("1");
            }
            // cout << " all " << mains << "\n";
            do{
                vector<ll> nums;
                nums.clear();
                ll x;
                string str = so + mains + se;
                for( x = 2 ; x <= 10 ; x++ ){
                    theNum = calc(str, x);
                    if(isNotPrime(theNum)){
                        nums.pb(toSend);
                    }
                    else{
                        goto there;
                    }
                }
                cout << str << " ";
                for ( ll ix = 0 ; ix < 9 ; ix ++ ){
                    cout << nums[ix] << " ";
                }
                nums.clear();
                cout << "\n";
                J -- ;
                if ( J == 0 ){
                    return 0;
                }
                there:;
                // cout << mains << endl;
            }while(next_permutation(all(mains)));
        }
    }
    return 0;
}