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

string s,t;
void in(){
	
	cin>>s;
	
	
}
string make(ll x,string y){
	if(x==s.length()) return y;
    string e=""; e+=s[x]; 
    if((y+e)>(e+y)) y=(y+e);
    else y=(e+y);
	return make(x+1,y);
}
void solve(){
	
	
	cout<<make(0,"")<<endl;
	
}



int main(){
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
//cout << setprecision(22) << fixed;
ios::sync_with_stdio(false);


ll tst ;cin>>tst;

F(i,1,tst){
	in();
	cout<<"Case #"<<i<<": ";
	solve();
}





return 0;   
}
