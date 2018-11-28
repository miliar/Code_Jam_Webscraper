#include <bits/stdc++.h>
#define rep(i,a,n) for(int i=a;i<n;i++)
#define repb(i,a,b) for(int i=a;i>=b;i--)
#define all(a) a.begin(),a.end()
#define o(a) cout<<a<<endl
#define int long long
#define fi first
#define se second
using namespace std;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;

signed main(){
	int t;
	cin>>t;
	rep(x,0,t){
		string s,t="";
		cin>>s;
		t+=s[0];
		rep(i,1,s.size()){
			if(s[i]>=t[0]) t=s[i]+t;
			else t=t+s[i];
		}
		cout<<"Case #"<<x+1<<": "<<t<<endl;
	}
}