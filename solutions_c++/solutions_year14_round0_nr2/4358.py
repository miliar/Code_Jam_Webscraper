#include<bits/stdc++.h>
using namespace std;
#define F(n) FO(i,n)
#define FO(i,n) FI(i,0,n)
#define FI(i,f,l) for(int i=(f),ei=(l);i<ei;i++)
const int mx=1e5;double c,f,x;
double F[1+mx],G[1+mx];
double lb(double c,double f,double x){
	F[0]=0;
	G[0]=x/2;
	for(int k=1;k<=x;k++){
		F[k]=F[k-1]+c/(2+(k-1)*f);
		G[k]=F[k]+x/(2+k*f);
		if(G[k]>G[k-1])
			return G[k-1];
	}
}
int main(){
	//freopen("i.txt","r",stdin);
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t;cin>>t;
	F(t){
		printf("Case #%i: ",i+1);
		cin>>c>>f>>x;
		printf("%.7f\n",lb(c,f,x));
	}
	return 0;
}
/*

c: cookies cost of a farm
f: cookies count of a farm produce per second
x: objective of count of cookies

t: time to accomplish the objective

Ans: minimumu t



*/
