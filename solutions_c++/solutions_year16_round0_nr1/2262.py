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
ll t,n,x;
bool b[10];
bool check(){
    for(int i=0;i<10;i++){
        if(!b[i])
            return 0;
    }
    return 1;
}
void F(ll num){
    while(num){
        b[num%10]=1;
        num/=10;
    }
}
int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    fin>>t;
    for(int i=1;i<=t;i++){
        fin>>n;
        x=n;
        fout<<"Case #"<<i<<": ";
        if(n==0)
            fout<<"INSOMNIA"<<endl;
        else{
            while(!check()){
                F(x);
                x+=n;
            }
            fout<<x-n<<endl;
            for(int i=0;i<10;i++) b[i]=0;
        }
    }
    return 0;
}
