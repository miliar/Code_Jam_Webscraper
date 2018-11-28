#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	int a[10][10],b[10][10];int T;cin>>T;
	int tt=0;
	while(T--){
		bool c[20];memset(c,0,sizeof c);
		int n,m;cin>>n;
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++){
				cin>>a[i][j];
			}
		cin>>m;
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++){
				cin>>b[i][j];
			}
		for(int i=1;i<=4;i++){
			c[a[n][i]]=1;
		}
		int ans=0;int fin=0;
		for(int i=1;i<=4;i++){
			if(c[b[m][i]]==1){ans++;fin=b[m][i];}
		}
		cout<<"Case #"<<++tt<<": ";
		if(ans==1){
			cout<<fin<<endl;
		}else if(ans>1){
			cout<<"Bad magician!"<<endl;
		}else cout<<"Volunteer cheated!"<<endl;
	}
	return 0;
}