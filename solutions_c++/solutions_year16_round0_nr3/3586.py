#include<iostream>
#include<fstream>
#include<string>
#include<cstring>
#include<math.h>
#include<cassert>
#include<iomanip>
#include<algorithm>
#include<vector>
#include<map>
#include<queue>
#include<stack>
#include<set>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<bitset>
#include<valarray>
#include<iterator>
#include<list>
#define ll long long
#define ull unsigned long long
#define mp make_pair
#define S second
#define F first
#define y1 LOL
#define pb push_back
#define len length
#define sz size
#define beg begin
const int inf=(int)1e9; 
const int mod=1e9+7;
using namespace std;
ll n,len,t;
ll to_system(string s,int k){
	ll h=1;
	ll sum=0;
	for(int i=s.len()-1;i>=0;i--){
		if(s[i]=='1'){
			sum+=h;
		}
		h*=k;
	}
	return sum;
}
string to_binary(ll x){
	string s="";
	while(x){
		s=(char)(x%2+48)+s;
		x/=2;
	}
	return s;
}
ll check(ll x){
	ll mx=0;
	for(int i=2;i<=sqrt(x);i++){
		if(x%i==0){
			mx=i;
		}
	}
	return mx;
}
vector<ll> a[511];
int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	//cout.tie(0);
	//freopen(".in","r",stdin);
	freopen("c.out","w",stdout);
	cin>>t;
	cin>>n>>len;
	int sz=0;
	for(int i=(1<<(n-1));i<(1<<n)&&len>sz;i++){
		string s=to_binary(i);
		bool z=0;
		vector<ll> g;
		g.pb(i);
		for(int j=2;j<=10;j++){
			ll k=to_system(s,j);
			ll di=check(k);
			if(!di){
				z=1;
				break;
			}
			g.pb(di);
		}
		if(!z&&s[s.len()-1]=='1'){
			a[++sz]=g;
		}
	}
	cout<<"Case #1:\n";
	for(int i=1;i<=sz;i++){
		cout<<to_binary(a[i][0])<<" ";
		for(int j=1;j<a[i].sz();j++){
			cout<<a[i][j]<<" ";
		}
		cout<<endl;
	}
	//cout<<to_system("110111",3);
	/*for(int i=2;i<=10;i++){
		cout<<to_system("1001",i)<<" ";
	}*/
	return 0;
}