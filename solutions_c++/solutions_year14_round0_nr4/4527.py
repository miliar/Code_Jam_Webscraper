#include<iostream>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<cstdio>
#include<functional>
#include<cstdlib>
#include<ctime>
#include<cassert>
#include<iomanip>
#include<string>
#include<cstring>
#include<cctype>
#include<cmath>
 #include<iterator>
using namespace std;
typedef long long ll;
#define FRN(i,a,b) for(ll i=a;i<(ll)b;i++)
#define pb push_back
#define mp make_pair 
typedef  vector<ll> vi;
typedef  vector<vector<ll> > vvi;
typedef  vector<string> vs;
typedef  vector<double> vd;
typedef  pair<ll,ll> pi;
typedef  map<ll,ll> mii;
typedef  map<string,ll> msi;
typedef  map<ll,string> mis;
typedef  vector<pair<int,int> > vp;
typedef  set<ll> si;
typedef  set<string> ss;
typedef long long ll;
const int Max = 10000;
int minp[Max + 1];
template <class T>
T minf(T a,T b){
	if(a<b)return a;
	else b;
}

main(){
	freopen("D-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	ll T;
	cin>>T;
	ll C=1;
	while(T--){
		double n;
	cin>>n;	
	vector<double> v1(n),v2(n);
	for(int i=0;i<n;i++){
	cin>>v1[i];}
	for(int i=0;i<n;i++){
	cin>>v2[i];}
	sort(v1.begin(),v1.end());
	sort(v2.begin(),v2.end());
	ll ans2=0,ans1=0;	
	for(int i=0,j=0;i<n;i++){
		if(v2[i]<v1[j])continue;
		else {
		j++;ans2++;
		}
	}
	ll ccc;
	while(1){
		ans1=0;
	for(int i=0,j=0;i<v1.size();i++){
		
		if(v2[i]<v1[j]){
		}
		else{
		j++;
		ans1++;
		}
	}
	 ccc=0;
	for(int i=0;i<v1.size();i++){
		if(v1[i]>v2[i])ccc++;
	}
	if(ccc==v1.size())break;
	//cout<<v1[0]<<"  "<<v2[v2.size()-1];
	v1.erase(v1.begin());
	v2.erase(v2.begin()+v2.size()-1);
	}
	cout<<"Case #"<<C<<": "<<ccc<<" "<<n-ans2<<endl;
	C++;
}
}
