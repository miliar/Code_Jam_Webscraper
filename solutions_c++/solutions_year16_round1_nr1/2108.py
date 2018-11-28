#include<bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef pair<int,int> PII;
#define MP make_pair
#define PB push_back
#define AA first
#define BB second
#define OP begin()
#define ED end()
#define SZ size()
#define cmin(x,y) x=min(x,y)
#define cmax(x,y) x=max(x,y)
#define NAME "A-small-attempt0"
#define UsingFile 1
const LL MOD = 1000000007;
const double PI = acos(-1.);
string solve(string s){
	if(s.empty())return s;
	char mx=s[0];
	int i;
	for(i=0;i<s.SZ;i++)
		cmax(mx,s[i]);
	string t;
	for(i=0;i<s.SZ;i++){
		if(s[i]==mx)break;
		t+=s[i];
	}
	string ret=solve(t);
	for(;i<s.SZ;i++){
		if(s[i]==mx)ret=s[i]+ret;
		else ret=ret+s[i];
	}
	return ret;
}
int main(){
    int i,j,k,_T;
    cin>>_T;
    for(int CA=1;CA<=_T;CA++){
    	string s;
    	cin>>s;
    	cout<<"Case #"<<CA<<": "<<solve(s)<<"\n"; 
    }
    return 0;
}