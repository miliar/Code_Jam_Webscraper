#include <iostream>
#include <algorithm>
#include <string>
#include <math.h>
#include <fstream>
using namespace std;
#define fon(i,n) for(i=0;i<n;++i)
#define re return
#define ll long long
const double EPS = 1E-9;const int INF = 1000000000;const ll INF64 = (ll)1E18;const double PI = 3.1415926535897932384626433832795;

ll x,y;
typedef struct{ll l,r,d;}tpo;

int main()
{
	#ifndef ONLINE_JUDGE
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	#endif

	ll i,j,n,m,T,t,k;
	ll a[110][110],amin,imin,jmin;
	cin>>T;
	for(t=0;t<T;++t){
		cin>>n>>m;for(i=0;i<n;++i)for(j=0;j<m;++j)cin>>a[i][j];
		
		bool bOK=true;
		for(k=0;k<2*(n+m);++k){
			for(i=0,amin=100;i<n;++i)for(j=0;j<m;++j)if(a[i][j]<amin){amin=a[i][j];imin=i;jmin=j;}
			for(i=0;i<n;++i)
				if(a[i][jmin]>amin&&a[i][jmin]!=INF)break;
			for(j=0;j<m;++j)
				if(a[imin][j]>amin&&a[imin][j]!=INF)break;
			if(j<m&&i<n)bOK=false;
			else{
				if(j>=m)for(j=0;j<m;++j)a[imin][j]=INF;
				if(i>=n)for(i=0;i<n;++i)a[i][jmin]=INF;
			}
		}
		for(i=0;i<n&&bOK;++i)for(j=0;j<m&&bOK;++j)if(a[i][j]!=INF)bOK=false;
		if(bOK)cout<<"Case #"<<t+1<<": "<<"YES"<<endl;
		else cout<<"Case #"<<t+1<<": "<<"NO"<<endl;
	}
	re 0;
}