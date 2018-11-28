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
vector<string> num;
vector<int> a;

void generate(string s,int n){
	if(n<=0){
		num.pb(s);
	}
	else{
		s[n-1]='0';
		generate(s,n-1);
		s[n-1]='1';
		generate(s,n-1);
	}
}

int convert(string s,ll base){
	  
	  reverse(s.begin(),s.end());
	  ll num=0;
	  ll k=0;
	  
	  for(int i=0;i<s.length();i++){
	  	num+=(pwr(base,k)*((ll)s[i]-'0'));
	  	k++;
	  }
	  //cout << s << " " << num << "\n";
	  
	  for(int i=2;i<sqrt(num)+1;i++){
	  	if(num%i==0){
	  		a.pb(i);
	  		return 1;
	  	}
	  }
	  return 0;
}

int main(){
	
	int T;
	cin >> T;

	for(int t=1;t<=T;t++){

		cout << "Case #" << t << ": " << "\n";
		int n,j;
		
		cin >> n >> j; 
		
		string tmp;
		tmp.resize(n);
		generate(tmp,n);

		int cnt=1;
		//int x=convert(tmp,2);
	
		for(int i=0;i<pwr(2,n) && cnt<=j;i++){	
			
			string str=num[i];
			if(str[0]=='1' && str[n-1]=='1'){

				bool pos=true;
				for(ll j=2;j<=10;j++){
					if(!convert(num[i],j)){
						pos=false;
						break;
					}
				}
				if(pos){
					cout << num[i] << " ";
					for(int k=0;k<9;k++)
						cout << a[k] << " ";
					cnt++;
					cout << "\n";
				}	
			}
			a.clear();
		}
	 }
	return 0;
}