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

int ssum[150];

int main(){
	
	int T;
	cin >> T;

	for(int t=1;t<=T;t++){
		
		cout << "Case #" << t << ": ";
		string s;
		cin >> s;

		if(s.length()==1){
			if(s[0]=='-')
				cout << 1 << "\n";
			else cout << 0 << "\n";
			continue;
		}
		memset(ssum,0,sizeof(ssum));
		ssum[s.length()-1]=1;

		for(int i=s.length()-2;i>=0;i--){
			if(s[i]==s[i+1])ssum[i]=ssum[i+1]+1;
			else ssum[i]=1;
		}

		//for(int i=0;i<s.length();i++)cout << ssum[i] << " ";


		int cntn=0,cntp=0,ans=0;
		if(s[0]=='-')cntn=1;
		else cntp=1;

		for(int i=1;i<s.length();){
			if(s[i]=='-'){
				if(cntp){
					ans+=2;
					i+=ssum[i];
					cntp=1;
					cntn=0;
				}
				else{
					cntn=1;
					i++;
				}
			}
			if(s[i]=='+'){
				if(cntn){
					ans+=1;
					i+=ssum[i];
					cntn=0;
					cntp=1;
				}
				else{
					cntp=1;
					i++;
				}
			}
		}
		if(!ans && cntn)ans++;
		cout << ans << "\n";
	}	
	return 0;
}