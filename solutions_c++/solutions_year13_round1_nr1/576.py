#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
#include<vector>
#include<set>
#include<list>
#include<queue>
#include<cmath>
#include<functional>
#include<algorithm>
#define rep(i,n) for(int i=0;i<(n);i++)
using namespace std;

typedef unsigned long long ull;


ull bsearch(ull r,ull t){
	ull a1=2*r+1;
	ull lb=0,ub=min(1ull<<30,(1ull<<62)/a1);
	while(ub-lb>1){
		ull m =(lb+ub)/2;
		ull s= m*(a1+a1+(m-1)*4)/2;
		if(s<=t)lb=m;
		else ub=m;
	}
	return lb;
}
int main(){
	int T;
	ull r,t;
	cin>>T;
	rep(i,T){
		cin>>r>>t;
		cout<<"Case #"<<i+1<<": "<<bsearch(r,t)<<endl;
	}
	return 0;
}
