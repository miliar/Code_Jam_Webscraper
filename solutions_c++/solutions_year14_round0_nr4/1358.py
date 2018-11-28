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

static const double PI=6*asin(0.5);
typedef long long ll;
typedef complex<double> CP;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef vector<int> vint;
static const int INF=1<<24;

/*

0.186 0.389 0.907 0.832 0.959 0.557 0.300 0.992 0.899
0.916 0.728 0.271 0.520 0.700 0.521 0.215 0.341 0.458

0.186 0.300 0.389 0.557 0.832 0.899 0.907 0.959 0.992
0.215 0.271 0.341 0.458 0.520 0.521 0.700 0.728 0.916

0.186 0.300 0.389 0.557 0.832 0.899 0.907 0.959 0.992
0.215 0.271 0.341 0.458 0.520 0.521 0.700 0.728 0.916

4 1
*/
int main(){
	int T;
	cin>>T;
	rep(k,T){
		int n;
		cin>>n;
		vector<double> na(n),ke(n);
		rep(i,n){
			cin>>na[i];
		}
		rep(i,n){
			cin>>ke[i];
		}
		if(n==1){
			printf("Case #%d: ",k+1);
			if(na[0]<ke[0]){
				cout<<0<<" "<<0<<endl;
			}
			else{
				cout<<1<<" "<<1<<endl;
			}
			continue;
		}
		sort(ALL(na));
		sort(ALL(ke));
		/*
		rep(i,n){
			cout<<na[i]<<" ";
		}
		cout<<endl;
		rep(i,n){
			cout<<ke[i]<<" ";
		}
		cout<<endl;
		cout<<endl;
		*/
		int ans1=0,ans2=0;
		int tmp1,tmp2;
		
		rep(i,n/2+1){
			tmp1=0;
			rep(j,i){
				//cout<<j<<" "<<n-1-j<<endl;
				if(na[j]>ke[n-1-j]) tmp1++;
			}
			rep(j,n-i){
				//cout<<j+i<<" "<<j<<endl;
				if(na[j+i]>ke[j]) tmp1++;
			}
			//cout<<endl;
			ans1=max(ans1,tmp1);
		}
		
		//cout<<endl;
		/*
		rep(i,n){
			vector<double>::iterator it = upper_bound(ke.begin(),ke.end(),na[i]);
			if(it==ke.begin()){
				if(ke[0]==-1.0){
					*upper_bound(ke.begin(),ke.end(),0.0)=-1.0;
					ans2++;
				}
				else{
					ke[0]=-1.0;
				}
			}
			else{
				*it=-1.0;
			}
		}
		
		*/
		
		rep(i,n){
			int x=-1,y=-1;
			bool f=false;
			rep(j,n){
				if(na[i]<ke[j]){
					ke[j]=-1.0;
					f=true;
					break;
				}
				else if(ke[j]>0.0&&x<0) x=j;
			}
			if(!f){
				ke[x]=-1.0;
				ans2++;
			}
		}
		
		
		printf("Case #%d: ",k+1);
		cout<<ans1<<" "<<ans2<<endl;
	}
	return 0;
}