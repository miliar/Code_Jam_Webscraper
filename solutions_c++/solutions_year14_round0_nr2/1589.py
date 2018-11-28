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
	double C,F,X;
	cin>>T;
	reep(i,0,T){
		double ans=0.0;
		cin>>C>>F>>X;
		if(C>X) ans=X/2.0;
		else{
			double t1=X/2.0,t2;
			int c=1;
			while(1){
				t2=t1;
				t1=t2-X/(2.0+F*(c-1.0))+C/(2.0+F*(c-1.0))+X/(2.0+F*c);
				//cout<<t1<<endl<<t2<<endl;
				//cout<<endl;
				if(t1>=t2){
					ans=t2;
					break;
				}
				else{
					c++;
				}
			}
		}
		cout<<"Case #"<<i+1<<": ";
		printf("%.7f\n",ans);
	}
	return 0;
}