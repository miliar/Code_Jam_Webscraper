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
	int T;
	cin>>T;
	rep(o,T){
		printf("Case #%d: ",o+1);
		int a,b,k;
		cin>>a>>b>>k;
		map<int,int> ma;
		int ans=0;
		rep(i,a){
			rep(j,b){
				int t=(i)&(j);
				//cout<<t<<endl;
				if(t<k){
					ma[(i)&(j)]=1;
					ans++;
				}
			}
		}
		int tmp=a&b;
		//cout<<"   "<<tmp<<endl;
		cout<<ans<<endl;
		//cout<<ma.size()<<endl;
		//cout<<endl;
	}
	return 0;

}