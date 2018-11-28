#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#define rep(i,m) for(int i=0;i<(int)(m);i++)
using namespace std;
int T,N,M,arr[100][100];
int main(){
freopen("B-large.in","rt",stdin);
freopen("B-large.out","wt",stdout);
cin >> T;
rep(tt,T){cin>>N>>M;
	rep(i,N){
		rep(j,M){
			cin >> arr[i][j];
			}
		}
	bool psbl=true;
	rep(i,N){
		rep(j,M){
			bool row=true,col=true;
			rep(r,M)row=row&&(arr[i][j]>=arr[i][r]);
			rep(c,N)col=col&&(arr[i][j]>=arr[c][j]);
			if(!(row||col))psbl=false;
			}
		}

	cout<<"Case #"<<(tt+1)<<": ";
	if(psbl)cout<<"YES\n";
	else cout<<"NO\n";
	}
}
