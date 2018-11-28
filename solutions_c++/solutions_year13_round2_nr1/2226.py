#include <cstdio>
#include <cmath>
#include <iostream>
#include <sstream>
#include <queue>
#include <map>
#include <algorithm> 
#include <vector>
#include <string>
#include <string.h>
#include <limits.h>
#define FOR(i,n) for(int i=0;i<(n);i++)
#define FORR(i,n) for(int i=(n)-1;i>=0;i--)
#define MAX 105

using namespace std;




int A,N,T;
int v[MAX];

int count(long m,long v,long& r){
	if(m==1) return INT_MAX;
	int i=0;
	while(m<=v){ m+=m-1; i++;}
	r=m;
	return i;
}

int solve(){
	sort(v,v+N);
	long r=0,m=A;
	FOR(i,N){
		if(v[i]<m) m+=v[i];
		else{
			long cr=0;
			long c=count(m,v[i],cr);
			int left=N-i;
			if(left<=c) return r+left;
			m=cr+v[i];
			r+=c;
		}
	}
	return r;
}


int main(){
	// freopen("input.txt","r",stdin);
	cin>>T;
	FOR(t,T){
		cin>>A>>N;		
		FOR(i,N)	cin>>v[i];	
		int r=solve();
		cout<<"Case #"<<(t+1)<<": "<<r<<endl;
	}
	
}
