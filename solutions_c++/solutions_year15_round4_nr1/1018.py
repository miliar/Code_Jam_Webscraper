#include <fstream>
#include <bits/stdc++.h>
using namespace std;
#define T pair<long long ,long long>
#define x first
#define y second
int main(){
	ifstream f1;
	ofstream f2;
	f1.open("input.txt");
	f2.open("output.txt");
	long long t,te,i,j,k,p,q,n,m,init,fin,vis[101][101],dir[4][2]={{-1,0},{1,0},{0,-1},{0,1}};
	string inp[101];
	f1>>t;
	for(te=0;te<t;te++){
		f1>>n>>m;
		fin=0;
		for(i=0;i<n;i++)f1>>inp[i];
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)vis[i][j]=0;
		for(i=0;i<n;i++){
			for(j=0;j<m;j++){
				if(inp[i][j]=='.')continue;
				if(inp[i][j]=='^')k=0;
				if(inp[i][j]=='v')k=1;
				if(inp[i][j]=='<')k=2;
				if(inp[i][j]=='>')k=3;
				p=i;
				q=j;
				while(1){
					p=p+dir[k][0];
					q=q+dir[k][1];
					if(p<0 ||p>=n || q<0||q>=m)break;
					if(inp[p][q]!='.')break;
				}
				if(p<0 ||p>=n || q<0||q>=m){
					for(p=i-1,q=j,init=0;p>=0;p--)if(inp[p][q]!='.')init++;
					for(p=i+1,q=j;p<n;p++)if(inp[p][q]!='.')init++;
					for(q=j-1,p=i;q>=0;q--)if(inp[p][q]!='.')init++;
					for(q=j+1,p=i;q<m;q++)if(inp[p][q]!='.')init++;
					if(init==0)break;
					fin++;
				}
			}
			if(j<m)break;
		}
		if(i<n){
			cout<<"Case #"<<(te+1)<<": IMPOSSIBLE\n";
			f2<<"Case #"<<(te+1)<<": IMPOSSIBLE\n";
			continue;
		}
		cout<<"Case #"<<(te+1)<<": "<<fin<<"\n";
		f2<<"Case #"<<(te+1)<<": "<<fin<<"\n";
	}
	f1.close();
	f2.close();
	return 0;
}
