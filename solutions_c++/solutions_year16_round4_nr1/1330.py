#include<bits/stdc++.h>
#define mod 1000000007
#include<bits/stdc++.h>
#define mod 1000000007
#define pp pair<ll,ll>
#define mp make_pair
#define ll long long
#define ff first
#define ss second
#define big 100000000000000000
using namespace std;

ll tc,n,r_,p,s;
char arr[1000010];
string ans,str;

string print(ll l,ll r){
	if(l == r){
		string str = "";
		str = str+arr[l];
		return str;
	}
	ll mid = (l+r)/2;
	string str1 = print(l,mid);
	string str2 = print(mid+1,r);
	if(str1 < str2)
		return str1+str2;
	else
		return str2+str1;
}
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	ios::sync_with_stdio(0);
	
	cin>>tc;
	for(ll t=1;t<=tc;t++){
		cin>>n>>r_>>p>>s;
		
		str="";
		ans="";
		
		//P is winner
		arr[0] = 'P';
		ll l = 0;
		ll r = 0;
		for(ll i=1;i<=n;i++){
			for(ll j=l;j<=r;j++){
				if(arr[j] == 'P'){
					arr[2*j+1] = 'P';
					arr[2*j+2] = 'R';
				}
				else if(arr[j] == 'R'){
					arr[2*j+1] = 'R';
					arr[2*j+2] = 'S';
				}
				else{
					arr[2*j+1] = 'P';
					arr[2*j+2] = 'S';
				}
			}
			l = 2*l+1;
			r = 2*r+2;
		}
		ll P=0,R=0,S=0;
		for(ll j=l;j<=r;j++){
			if(arr[j] == 'P')
				P++;
			else if(arr[j] == 'R')
				R++;
			else
				S++;
		}
	/*	cout<<l<<" "<<r<<" "<<P<<" "<<R<<" "<<S<<" "<<"\n";
		for(ll j=l;j<=r;j++)
			cout<<arr[j];
		cout<<"\n";
		cout<<p<<" "<<r<<" "<<s<<"\n";
		cout<<(p==P)<<" "<<(r==R)<<" "<<(s==S)<<"\n";
	*/	if(p == P && r_ == R && s == S){
			str = print(l,r);
			if(ans == "")
				ans = str;
			else
				ans = min(ans,str);
		//	cout<<str<<"\n";
		}
		
		//S is winner
		arr[0] = 'S';
		l = 0;
		r = 0;	
		for(ll i=1;i<=n;i++){
			for(ll j=l;j<=r;j++){
				if(arr[j] == 'P'){
					arr[2*j+1] = 'P';
					arr[2*j+2] = 'R';
				}
				else if(arr[j] == 'R'){
					arr[2*j+1] = 'R';
					arr[2*j+2] = 'S';
				}
				else{
					arr[2*j+1] = 'P';
					arr[2*j+2] = 'S';
				}
			}
			l = 2*l+1;
			r = 2*r+2;
		}
		P=0,R=0,S=0;
		for(ll j=l;j<=r;j++){
			if(arr[j] == 'P')
				P++;
			else if(arr[j] == 'R')
				R++;
			else
				S++;
		}
	/*	cout<<l<<" "<<r<<" "<<P<<" "<<R<<" "<<S<<" "<<"\n";
		for(ll j=l;j<=r;j++)
			cout<<arr[j];
		cout<<"\n";
	*/	if(p == P && r_ == R && s == S){
			str = print(l,r);
			if(ans == "")
				ans = str;
			else
				ans = min(ans,str);
		//	cout<<str<<"\n";
		}
		
		//R is winner
		arr[0] = 'R';
		l = 0;
		r = 0;	
		for(ll i=1;i<=n;i++){
			for(ll j=l;j<=r;j++){
				if(arr[j] == 'P'){
					arr[2*j+1] = 'P';
					arr[2*j+2] = 'R';
				}
				else if(arr[j] == 'R'){
					arr[2*j+1] = 'R';
					arr[2*j+2] = 'S';
				}
				else{
					arr[2*j+1] = 'P';
					arr[2*j+2] = 'S';
				}
			}
			l = 2*l+1;
			r = 2*r+2;
		}
		P=0,R=0,S=0;
		for(ll j=l;j<=r;j++){
			if(arr[j] == 'P')
				P++;
			else if(arr[j] == 'R')
				R++;
			else
				S++;
		}
	/*	cout<<l<<" "<<r<<" "<<P<<" "<<R<<" "<<S<<" "<<"\n";
		for(ll j=l;j<=r;j++)
			cout<<arr[j];
		cout<<"\n";
	*/	if(p == P && r_ == R && s == S){
			str = print(l,r);
			if(ans == "")
				ans = str;
			else
				ans = min(ans,str);
		//	cout<<str<<"\n";
		}
		if(ans == "")
			cout<<"Case #"<<t<<": IMPOSSIBLE\n";
		else
			cout<<"Case #"<<t<<": "<<ans<<"\n";
	}
	return 0;
}

