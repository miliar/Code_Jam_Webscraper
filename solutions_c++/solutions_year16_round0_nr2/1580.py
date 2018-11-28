// IN THE NAME OF ALLAH
#include<bits/stdc++.h>
#define pb push_back
#define X first
#define Y second
#define F(i,a,b) for(ll i=(a) ; i<=(b) ; i++)
#define PI 3.1415926535897932384626433832795
#define eps 0.000001
using namespace std;
typedef long long ll;
typedef float ld;
const ll M=1e5+100;

string rev(string s){
	string t=s;
	F(i,0,s.length()-1){
		if(s[i]=='+') t[i]='-';
		else t[i]='+';
	}
	return t;
}

ll proc(string s){
	//cout<<s<<endl;
	ll sz=s.length()-1;
	bool b=false;
	F(i,0,sz) if(s[i]=='-') b=true;
	if(!b) return 0;
	if(s=="-") return 1;
	if(s[sz]=='-'){
		s.erase(sz,1);
		s=rev(s);
		return proc(s)+1;
	}
	else{
		s.erase(sz,1);
		return proc(s);
	}
}


int main(){
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
//cout << setprecision(22) << fixed;
ios::sync_with_stdio(false);


ll tst; cin>>tst;
string s;
F(i,1,tst){
	cin>>s;
	cout<<"Case #"<<i<<": "<<proc(s)<<endl;
}



return 0;   
}
