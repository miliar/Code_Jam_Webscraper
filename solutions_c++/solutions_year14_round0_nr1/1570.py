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
#define rep(i,n) reep(i,0,n)
#define ALL(v) (v).begin(),(v).end()
#define PB push_back
#define EPS 1e-8
#define F first
#define S second

static const double PI=6*asin(0.5);
typedef long long ll;
typedef complex<double> CP;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef vector<int> vint;
static const int INF=1<<24;


/*
C,F,X
t=X/2
t=C/2+X/(2+F)
t=C/2+C/(2+F)+C/(2+2*F)

15+7.5+5+
*/

int main(){
	int T;
	int a[5][5];
	int b[5][5];
	int aa,ba;
	cin>>T;
	rep(k,T){
		cin>>aa;
		rep(i,4){
			rep(j,4){
				cin>>a[i][j];
			}
		}
		cin>>ba;
		rep(i,4){
			rep(j,4){
				cin>>b[i][j];
			}
		}
		int ac[20]={0},bc[20]={0};
		rep(i,4){
			ac[a[aa-1][i]]++;
			bc[b[ba-1][i]]++;
		}
		int ans=-1;
		rep(i,16){
			if(ac[i+1]==1&&bc[i+1]==1){
				if(ans<0) ans=i+1;
				else if(ans>0){
					ans=-2;
					break;
				}
			}
		}
		printf("Case #%d: ",k+1);
		if(ans>0) cout<<ans<<endl;
		else if(ans==-2) cout<<"Bad magician!"<<endl;
		else if(ans==-1) cout<<"Volunteer cheated!"<<endl;
	}
	return 0;
}