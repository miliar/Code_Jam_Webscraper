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


main(){
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	ll T,grid1[4][4];
	cin>>T;
	ll C=1;
		while(T--){
			ll a;
			cin>>a;
			map<ll,bool> m;
			for(int i=0;i<4;i++){
				for(int j=0;j<4;j++){
					cin>>grid1[i][j];
					if(i+1==a){
						m[grid1[i][j]]=1;
					}
				}
			}
			ll b;
			cin>>b;
			ll res=0,ans=0;
			for(ll i=0;i<4;i++){
				for(ll j=0;j<4;j++){
					cin>>grid1[i][j];
					if(i+1==b){
						if(m[grid1[i][j]]){
						ans=grid1[i][j];
						res++;
						}
					}
				}
			}
			if(res==1){
				cout<<"Case #"<<C<<": "<<ans<<endl;
			}
			if(res>1){
				cout<<"Case #"<<C<<": "<<"Bad magician!"<<endl;
			}
			if(res==0){
				cout<<"Case #"<<C<<": Volunteer cheated!"<<endl;
			}
			C++;
		}
		
}
