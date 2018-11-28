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
const ll maxn=2*1e8+1,inf=1e9+1,del=1e9+7;
ll t,k,c,s;
int main(){
    ios_base::sync_with_stdio(0);fin.tie(0);fout.tie(0);
    fin>>t;
    for(int i=1;i<=t;i++){
        fout<<"Case #"<<i<<": ";
        fin>>k>>c>>s;
        for(int j=1;j<=s;j++) fout<<j<<" ";
        fout<<endl;
    }
    return 0;
}
