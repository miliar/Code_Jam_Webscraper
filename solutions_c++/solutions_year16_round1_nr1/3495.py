#include<bits/stdc++.h>
#define ll long long
using namespace std;

const ll MOD = 1e9+7;

ll power(ll base,ll exp){
    ll ret=1;
    while(exp>0){
        if(exp&1)ret=(ret*base)%MOD;
        base=(base*base)%MOD;
        exp>>=1;
    }
    return ret;
}

ll inverse(ll a){
    return power(a,MOD-2);
}

//bool cmp(const pair< ll,int > &a,const pair< ll,int > &b){
//	if(a.first-tim==b.first-tim){
//		return a.second<b.second;
//	}
//	return a.first-tim<b.first-tim;
//}

ll hcf(ll a,ll b){
	if(a<b)swap(a,b);
	if(b==0)return a;
	return hcf(b,a%b);
}

vector < string > v;

void rec(string s,string z){
	if(z==""){
		z+=s[0];
		rec(s.substr(1),z);
		return;
	}
	if(s.length()==1){
		v.push_back(z+s[0]);
		v.push_back(s[0]+z);
		return;
	}
	rec(s.substr(1),z+s[0]);
	rec(s.substr(1),s[0]+z);
}

int main(){
	
	ll t,n,b,k,i,j;
	cin>>t;
	string s;
	for(i=1;i<=t;i++){
		cin>>s;
		string st="";
		st+=s[0];
		for(int j=1;j<s.length();j++){
			if(s[j]>=st[0])st=s[j]+st;
			else st=st+s[j];
		}
		cout<<"Case #"<<i<<": "<<st<<"\n";
	}
	return 0;
}
