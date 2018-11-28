#include<bits/stdc++.h>
using namespace std;

#define inf (1000000007)
#define pii pair<int,int>
#define ppi pair<pii,int>
#define ppp pair<pii,pii>
#define ll long long 
#define pb push_back
#define vi vector<int>
#define vii vector< vector<int> >
#define mp make_pair
#define s(n) scanf("%d",&n)
#define s2(n,m) scanf("%d%d",&n,&m)
#define s3(n,m,l) scanf("%d%d%d",&n,&m,&l)
#define rep(i,n) for(int i=0;i<n;++i)
ll pwr(ll a,ll b,ll mod) {a%=mod;if(a<0)a+=mod;ll ans=1; while(b) {if(b&1) ans=(ans*a)%mod; a=(a*a)%mod; b/=2; } return ans; }
ll pwr(ll a,ll b) {ll ans=1; while(b) {if(b&1) ans*=a; a*=a; b/=2; } return ans; }
ll gcd(ll a,ll b) {while(b) {ll temp=a; a=b; b=temp%b; } return a; }
ll lcm(ll a,ll b) {return (a/gcd(a,b))*b; }
string toString(int j){string s = "";while(j){int temp=j%10;s+=temp+'0';j=j/10;}reverse(s.begin(),s.end());return s;}
ll modularInverse(ll a,ll m) {/*reminder: make sure m is prime*/ assert(false); return pwr(a,m-2,m); }
bool prime(ll x){if (x < 2) return false;for(ll i=2; i<= sqrt(x); i++) {if ((x%i) == 0) return false;}return true;}
const int mod=1000000007;

int main(){
 //ios::sync_with_stdio(0);


int test,smax;
cin >> test;

string s;

for(int t=1;t<=test;t++){
    printf("Case #%d: ",t);
    
    cin >>  smax >> s;
    int ans=0,there=0;

    for(int i=0;i<=smax;i++){

            if(there>=i){
            there+=s[i]-'0';
            }
            else{
                ans+=(i-there);
                there+=(i-there)+(s[i]-'0');
            }
            
            //cout << i << " " << ans << endl;
        }

        cout << ans << endl;

 }
 return 0;
 }

