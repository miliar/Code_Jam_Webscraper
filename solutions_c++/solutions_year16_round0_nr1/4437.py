// By - irajdeep		
#include <bits/stdc++.h>
using namespace std;
#define ios ios_base::sync_with_stdio(false);cin.tie(NULL);
#define infinity (1000000007)
#define eps 1e-12
#define ll long long
#define ull unsigned long long
#define vi vector<int>
#define pii pair<int,int>
#define pb push_back
#define mp make_pair
ll pwr(ll a,ll b,ll mod) {a%=mod;if(a<0)a+=mod;ll ans=1; while(b) {if(b&1) ans=(ans*a)%mod; a=(a*a)%mod; b/=2; } return ans; }
ll pwr(ll a,ll b) {ll ans=1; while(b) {if(b&1) ans*=a; a*=a; b/=2; } return ans; }
ll gcd(ll a,ll b) {while(b) {ll temp=a; a=b; b=temp%b; } return a; }
ll lcm(ll a,ll b) {return (a/gcd(a,b))*b; }
string toString(int j){string s = "";while(j){int temp=j%10;s+=temp+'0';j=j/10;}reverse(s.begin(),s.end());return s;}
ll modularInverse(ll a,ll m) {/*reminder: make sure m is prime*/ assert(false); return pwr(a,m-2,m); }
const int mod=1000000007;

int arr[10];

int all(){

	for(int i=0;i<=9;i++){
		if(!arr[i])return 0;
	}
	return 1;
}

int main(){
	
	int T;
	cin >> T;

	for(int t=1;t<=T;t++){
		
		cout << "Case #" << t << ": ";
		
		memset(arr,0,sizeof(arr));
		ll n;
		cin >> n;
		
		if(n==0){
			cout << "INSOMNIA\n";
		}
		else{
			int k=1;
			ll num,ans;

			while(!all()){
				num=n*k;
				ans=num;
				k++;

				while(num){
					int x=num%10;
					num=num/10;
					arr[x]=1;
				}
			}
			cout << ans << "\n";
		}
	}	
	return 0;
}