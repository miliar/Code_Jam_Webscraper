#include<iostream>
#include<stdio.h>
#include<string.h>
#define fr(i,a,b) for(i=a;i<=b;++i)
using namespace std;
const int maxn=102;
int g[maxn][maxn],row[maxn],col[maxn],ti,ca,i,j,n,m;
bool ok;
int main(){
	freopen("b2.in","r",stdin);
	freopen("b2.out","w",stdout);
	cin>>ca;
	fr(ti,1,ca){
		cin>>n>>m;
		memset(row,0,sizeof(row));
		memset(col,0,sizeof(col));
		fr(i,1,n)
			fr(j,1,m){
				cin>>g[i][j];
				row[i]=max(row[i],g[i][j]);
				col[j]=max(col[j],g[i][j]);
			}
		ok=true;
		fr(i,1,n)
			fr(j,1,m)
				if(g[i][j]!=min(row[i],col[j]))
					ok=false;
		if(ok)
			cout<<"Case #"<<ti<<": YES"<<endl;
		else
			cout<<"Case #"<<ti<<": NO"<<endl;
	}
}