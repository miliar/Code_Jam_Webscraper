#include <cstdio>
#include <cmath>
#include <iostream>
#include <sstream>
#include <queue>
#include <map>
#include <vector>
#include <string>
#include <string.h>
#include <limits.h>
#define FOR(i,n) for(int i=0;i<(n);i++)
#define FORR(i,n) for(int i=(n)-1;i>=0;i--)
#define MAX 120
#define MOD 1000000
#define LL long long
#define PR pair<int,int>
#define MAP map<int,int>
#define VI vector<int>
#define PQUEUE priority_queue<PR >
#define FORM(i,n) for(MAP::iterator i=n.begin();i!=n.end();i++)
using namespace std;



int M,N,T;
int dp[MAX][MAX],l[MAX],r[MAX];
bool solve(){
	FOR(i,N){ 
		l[i]=dp[i][0];
		FOR(j,M) l[i]=max(l[i],dp[i][j]);
	}
	FOR(j,M){ 
		r[j]=dp[0][j];
		FOR(i,N) r[j]=max(r[j],dp[i][j]);
	}
	FOR(i,N)FOR(j,M){
		if(dp[i][j]<l[i] && dp[i][j]<r[j]) return false;
	}
	return true;
}

int main(){
	N=4;
	//scanf("%d",&T);
	cin>>T;
	FOR(test,T){	
		cin>>N>>M;
		FOR(i,N)
			FOR(j,M)
			//scanf("%c",&dp[i][j]);			
			cin>>dp[i][j];
		
		bool r=solve();
		cout<<"Case #"<<(test+1)<<": ";
		if(r) cout<<"YES"<<endl;
		else  cout<<"NO"<<endl;		
	}
	
}
