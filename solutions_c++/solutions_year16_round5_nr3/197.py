#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <iostream>
#define maxn 1009
#define PS system("pause");
using namespace std;
int n,S;
int X[maxn],Y[maxn],Z[maxn];
int p[maxn];
int findset(int x){
	return x==p[x]?x:p[x]=findset(p[x]);
}
void unionset(int x,int y){
	p[findset(x)]=findset(y);
}
double sqr(double x){
	return x*x;
}
double dis(int i,int j){
	return sqrt(sqr(X[i]-X[j])+sqr(Y[i]-Y[j])+sqr(Z[i]-Z[j]));
}
bool check(double m){
	for(int i=0;i<n;i++)
		p[i]=i;
	for(int i=0;i<n;i++)
		for(int j=i+1;j<n;j++){
			if(dis(i,j)<=m)
				unionset(i,j);
		}
	return findset(0)==findset(1);
}
int main(){
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	int tt,cot=1;
	scanf("%d",&tt);
	while(tt--){
		scanf("%d%d",&n,&S);
		for(int i=0;i<n;i++){
			int a,b,c;
			scanf("%d%d%d%d%d%d",&X[i],&Y[i],&Z[i],&a,&b,&c);
		}
		double L=0,R=10000;
		for(int i=0;i<100;i++){
			double M=(L+R)/2;
			if(check(M))
				R=M;
			else
				L=M;
		}
		printf("Case #%d: %.7f\n",cot++,R);
	}
	return 0;
}