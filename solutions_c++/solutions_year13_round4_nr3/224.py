#include<iostream>
#include<stdio.h>
#include<cstring>
#include<vector>
#define fr(i,a,b) for(i=a;i<=b;i++)
const int maxn=1002;
using namespace std;
int n,list[maxn],in[maxn],i,j,k,a[maxn],b[maxn],ca,ti;
bool g[maxn][maxn];
bool ok(){
	int c[maxn],d[maxn],i,j;
	fr(i,1,n){
		c[i]=1;
		fr(j,1,i-1)
			if(list[j]<list[i]&&c[j]+1>c[i])
				c[i]=c[j]+1;
	}
	for(i=n;i>=1;i--){
		d[i]=1;
		fr(j,i+1,n)
			if(list[j]<list[i]&&d[j]+1>d[i])
				d[i]=d[j]+1;
	}
	fr(i,1,n)
		if(a[i]!=c[i]||b[i]!=d[i])
			return false;
	return true;
}
bool dfs(int r){
	if(r>n)
		return ok();
	int j,k;
	fr(j,1,n)
		if(in[j]==0){
			in[j]=-1;
			list[j]=r;
			vector<int> lst;
			fr(k,1,n)
				if(g[j][k]){
					g[j][k]=false;
					lst.push_back(k);
					in[k]--;
				}
			if(dfs(r+1))
				return true;
			in[j]=0;
			fr(k,0,(int)lst.size()-1){
				g[j][lst[k]]=true;
				in[lst[k]]++;
			}
		}
	return false;
}
int main(){
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	cin>>ca;
	fr(ti,1,ca){
		cin>>n;
		fr(i,1,n)
			cin>>a[i];
		fr(i,1,n)
			cin>>b[i];
		memset(g,0,sizeof(g));
		memset(in,0,sizeof(in));
		fr(i,1,n)
			fr(j,i+1,n){
				if(a[i]>=a[j]){
					g[j][i]=true;
					in[i]++;
				}
				if(b[i]<=b[j]){
					g[i][j]=true;
					in[j]++;
				}
			}
		fr(i,1,n-1)
			if(a[i]<a[i+1]&&g[i][i+1]==false){
				g[i][i+1]=true;
				in[i+1]++;
			}
		fr(i,1,n-1)
			if(b[i]>b[i+1]&&g[i+1][i]==false){
				g[i+1][i]=true;
				in[i]++;
			}				
		dfs(1);
		cout<<"Case #"<<ti<<":";
		fr(i,1,n)
			cout<<" "<<list[i];
		cout<<endl;
		//cout<<ok()<<endl;
	}
}