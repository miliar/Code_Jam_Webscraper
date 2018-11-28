#include <iostream>
#include <sstream>
#include <cstdio>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <cmath>
#include <algorithm>
#include <iomanip>
using namespace std;
#define sqr(x) ((x)*(x))
#define mp(x,y) make_pair((x),(y))
#define FOR(i,n) for(int i = 0 ; i<n ;i++)
#define f(i,x,y) for (int i = x; i < y; i++)
#define all(v) v.begin(),v.end()
#define pb push_back
#define sz(v) ((int)v.size())
#define fst first
#define snd second
#define itm1 fst.fst
#define itm2 fst.snd
#define itm3 snd
#define mt(a,b,c) mp(mp(a,b),c)
#define oo 2000000000

typedef long long ll  ;
typedef vector<int> vi ;
typedef pair<ll,ll> ill;
typedef pair<int,int> ii ;
typedef pair<ii, int> tri;

int sleep;
int res[10];

vi multiplicar(vi v,int t){
	int coloco=0;
	int lleva=0;
	vi ans;
	for(int j=v.size()-1;j>=0;j--){
		coloco=(v[j]*t + lleva) % 10;
		lleva=(v[j]*t + lleva)/10;
		ans.pb(coloco);
	}
	while(lleva){
		ans.pb(lleva%10);
		lleva/=10;	
	}
	return ans;
}

int main(){
	int t;
	string s;
	vi v,ans;
	cin>>t;
	int k=t;
	while(k--){
		cin>>s;
		v.clear();
		for(int i=0;i<s.size();i++){
			v.pb((int)s[i]-'0');
		}
		for(int i=0;i<10;i++){
			res[i]=0;
		}
		int c=1;
		sleep=0;
		int u=0;
		while(!sleep){
			if(s=="0"){
				u=1;
				break;
			}
			ans=multiplicar(v,c);
			for(int i=0;i<ans.size();i++){
				if(res[ans[i]]==0){
					res[ans[i]]++;
				}
			}
			for(int i=0;i<10;i++){
				if(res[i]==0){
					sleep=0;
					break;
				}
				sleep=1;
			}
			c++;
		}
		cout<<"Case #"<<abs(t-k)<<": ";
		if(u){
			cout<<"INSOMNIA";
		}
		else{
			for(int i=ans.size()-1;i>=0;i--){
				cout<<ans[i];
			}
		}
		cout<<endl;
	}
}