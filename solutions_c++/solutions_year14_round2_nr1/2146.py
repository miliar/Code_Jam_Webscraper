#include <iostream>
#include <queue>
#include <stack>
#include <vector>
#include <stdio.h>
#include <algorithm>
#include <string>
#include <cstring>
#include <cmath>
#include <complex>
#include <map>
#include <climits>
using namespace std;

#define reep(i,a,b) for(int i=(a);i<(b);++i)
#define rep(i,n) reep((i),0,(n))
#define ALL(v) (v).begin(),(v).end()
#define PB push_back
#define EPS 1e-8
#define F first
#define S second
#define mkp make_pair

static const double PI=6*asin(0.5);
typedef long long ll;
typedef complex<double> CP;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef vector<int> vint;
static const int INF=1<<24;


int main(){
	int T,n;
	cin>>T;
	rep(o,T){
		printf("Case #%d: ",o+1);
		int ans=0;
		cin>>n;
		bool f=false;
		string s[n];
		rep(i,n){
			cin>>s[i];
		}
		while(1){
			int oh=0;
			bool f1=false,f2=false;
			rep(i,n){
				if(s[i].size()!=0) f1=true;
				if(s[i].size()==0) f2=true;
			}
			
			if(f1&&f2){
				f=true;
				break;
			}
			if(!f1&&f2) break;
			int a[100]={0};
			int M=0;
			rep(i,n){
				if(s[0][0]!=s[i][0]){
					f=true;
					break;
				}
			}	
			rep(i,n){
				int c=0;
				rep(j,s[i].size()){
					if(s[i][0]!=s[i][j]) break;
					else c++;
				}
				a[i]=c;
				M=max(M,c);
				s[i]=s[i].substr(c);
			}
			if(f){
				
				break;
			}
			int tmp=1000;
			rep(i,M){
				int t=i+1;
				int tt=0;
				rep(j,n){
					tt+=abs(a[j]-t);
				}
				//cout<<tt<<endl;
				tmp=min(tmp,tt);
			}
			ans+=tmp;
		}
		if(f){
			cout<<"Fegla Won"<<endl;
			continue;
		}
		cout<<ans<<endl;
	}
	return 0;
}