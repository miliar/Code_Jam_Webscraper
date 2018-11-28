#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <map>
#include <vector>
#include <set>
#include <algorithm>
#include <sstream>
#include <queue>
#include <cctype>
#include <cmath>
#include <fstream>

using namespace std;

typedef long long ll;
#define REP(i,k) for(int (i)=0;(i)<(k);(i)++)
#define INF ~(1<<31)
#define CLR(a) memset((a),0,sizeof((a)))
#define EPS 1e-9
#define DBG 1
#define D(s,v) if(DBG) cout<<(s)<<": "<<(v)<<endl;
#define DVEC(s,v) if(DBG) {cout<<(s)<<": "; for(int i=0;i<(v).size();i++) cout<<(v)[i]<<" "; cout<<endl;}
#define DARR(s,v,n) if(DBG) {cout<<(s)<<": "; for(int i=0;i<n;i++) cout<<(v)[i]<<" "; cout<<endl;}

int main(){
ios_base::sync_with_stdio(0);

int T;
cin>>T;

for(int cs=1;cs<=T;cs++){
	int N,M;
	cin>>N>>M;
	int x[N][M];
	for(int i=0;i<N;i++)
	for(int j=0;j<M;j++)
		cin>>x[i][j];
		
	bool res=1;
	for(int i=0;i<N;i++)
	for(int j=0;j<M;j++)
	{
		bool f1=0,f2=0;
		for(int k=0;k<N;k++) if(x[k][j]>x[i][j]) f1=1;
		for(int k=0;k<M;k++) if(x[i][k]>x[i][j]) f2=1;
		if(f1 && f2) res=0;
	}
	
	cout<<"Case #"<<cs<<": ";
	if(res) cout<<"YES"<<endl;
	else cout<<"NO"<<endl;
}


}