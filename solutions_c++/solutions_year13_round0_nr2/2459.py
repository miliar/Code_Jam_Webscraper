#include <iostream>
#include <string>
#include <set>
#include <algorithm>
#include <stack>
#include <vector>
#include <math.h>
#include <iomanip>
#include <map>      // std::pair

#define FOR(i,s,e) for (int i=(s); i<(e); i++)
#define FOE(i,s,e) for (int i=(s); i<=(e); i++)
#define FOD(i,s,e) for (int i=(s)-1; i>=(e); i--)
#define CLR(a,x) memset(a, x, sizeof(a))
#define SIZE(v) ((int)(v).size())
#define FOREACH(i,v) for(typeof((v).begin()) i=(v).begin();i!=(v).end();i++)
typedef long long ll;
typedef std::pair<ll,ll> PII;
//typedef vector<PII> VPII;
using namespace std;

int a[101][101];
int n,m,t,maxa;

bool check(int i, int j, int k){
	bool cango=true;
	FOR(x,0,n){
		if (a[x][j]>k){
			cango=false;	
			break;
		}
	}
	if (cango){
		FOR(x,0,n)	a[x][j]=0;
	}
	bool cango2=true;
	FOR(x,0,m){
		if (a[i][x]>k){
			cango2=false;
			break;
		}
	}
	if (cango2){
		FOR(x,0,m)	a[i][x]=0;
	}
	return (cango||cango2);
}

void go(){
		maxa=0;
		CLR(a,0);
		cin>>n>>m;
		FOR(i,0,n)
			FOR(j,0,m){
				cin>>a[i][j];
				if (a[i][j]>maxa)	maxa=a[i][j];
			}
		FOE(k,1,maxa){
			FOR(i,0,n)
				FOR(j,0,m)	if (a[i][j]==k){
					if (!check(i,j,k)){
						cout<<"NO"<<endl;
						return;
					}
			
				}
		}
		cout<<"YES"<<endl;
		return;
}

int main(){
#ifndef ONLINE_JUDGE
	freopen("d.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
	cin>>t;
	FOR(tt,0,t){
		cout<<"Case #"<<tt+1<<": ";
		go();
	}

	return 0;

}