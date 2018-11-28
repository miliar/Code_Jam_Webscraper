//IN THE NAME OF ALLAH
//1395/01/21

#include <bits/stdc++.h>
#include <fstream>
#define mp make_pair
#define pb push_back
using namespace std;
ifstream fin("1.in");
ofstream fout("1.out");
typedef long long int ll;
typedef long double ld;
typedef pair < ll, ll > pii;
typedef vector < ll > vi;
typedef set < ll > si;
const ld pi=3.1415926535897932384626433832795028841971693993751;
const ll maxn=2*1e5+1,inf=1e9+1;
int t,ans;
string s;
bool b;
int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    fin>>t;
    for(int i=1;i<=t;i++){
        fin>>s;
        s.pb('+');
        b=0;
        ans=0;
        int si=s.size();
        for(int i=si-2;i>-1;i--){
            if(s[i]!=s[i+1])
                ans++;
        }
        fout<<"Case #"<<i<<": "<<ans<<endl;
    }
    return 0;
}
