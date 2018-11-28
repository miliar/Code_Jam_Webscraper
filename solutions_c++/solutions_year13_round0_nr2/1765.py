#include<iostream>
#include<string>
using namespace std;
int lawn[200][200];
string cut(int n,int m){
	for(int i=1;i<=n;++i){
		for(int j=1;j<=m;++j){
			int h = lawn[i][j];
			int sol = 0;
			for(int pos=1;pos<=n;++pos){
				if(lawn[pos][j]>h){sol++;break;}
			}
			for(int pos=1;pos<=m;++pos){
				if(lawn[i][pos]>h){sol++;break;}
			}
			if(sol==2)return "NO";
		}
	}
	return "YES";
}
void solve(){
	int t,n,m;
	cin>>t;
	for(int k=1;k<=t;++k){
		cin>>n>>m;
		for(int i=1;i<=n;++i)for(int j=1;j<=m;++j)cin>>lawn[i][j];
		cout<<"Case #"<<k<<": "<<cut(n,m)<<endl;
	}
}
int main(){
	solve();
}