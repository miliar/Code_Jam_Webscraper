#include<iostream>
#include<cstdio>
#include<cmath>
#define fr(i,a,b) for(i=a;i<=b;++i)
using namespace std;
long long ca,ti,r,t,ans;
long long find(long long a,long long b){
	if(a==b)
		return a;
	long long mid2=(a+b)/2+1;
	if((1+2*r)+(mid2-1)*2<=t/mid2)
		return find(mid2,b);
	else
		return find(a,mid2-1);
}
int main(){
	freopen("a2.in","r",stdin);
	freopen("a2.out","w",stdout);
	cin>>ca;
	fr(ti,1,ca){
		cin>>r>>t;
		cout<<"Case #"<<ti<<": "<<find(1,1000000000)<<endl;
	}
}