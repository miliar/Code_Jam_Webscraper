/*Author:@abs51295*/
#include <bits/stdc++.h>
#include<fstream>
#define fr freopen("A-large.in","r",stdin)
#define fw freopen("A-large.out","w",stdout)
#define iOs ios_base::sync_with_stdio(false);
#define INF 1000000009
#define MOD 1000000007
#define all(x) (x).begin(), (x).end()
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;

main(){

        fw;fr;

    iOs;
    ll t; cin >> t;
    ll j=1;
    while(t--){
        ll n,i=2; cin >> n;
        ll y=n;
        bool b[10]={true,true,true,true,true,true,true,true,true,true};
        if(n==0){
            cout << "Case #" << j++ << ": " << "INSOMNIA" << endl;
        }
        else{
            while(b[0] || b[1] || b[2] || b[3] || b[4] || b[5] || b[6] || b[7] || b[8] || b[9]){
                ll x=n;
                while(x!=0){
                    int digit = x%10;
                    b[digit]=false;
                    x/=10;
                }
                n+=y;
            }
            cout << "Case #" << j++ << ": " << n-y << endl;
        }
    }
}
