#include<cstdio>
#include<iostream>
#include<vector>
using namespace std;
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w+",stdout);
	int T;
	cin>>T;
	for(int t=0;t<T;t++){
		cout<<"Case #"<<t+1<<": ";
		int N1,m1[4][4],N2,m2[4][4];
		cin>>N1;
		for(int i=0;i<4;i++)for(int j=0;j<4;j++) cin>>m1[i][j];
		cin>>N2;
		for(int i=0;i<4;i++)for(int j=0;j<4;j++) cin>>m2[i][j];
		int cont=0,sol;
		for(int i=0;i<4;i++)for(int j=0;j<4;j++) if(m1[N1-1][i]==m2[N2-1][j]) {
			cont++;
			sol=m1[N1-1][i];	
		}
		if(cont==1) cout<<sol;
		if(cont==0) cout<<"Volunteer cheated!";
		if(cont>1) cout<<"Bad magician!";
		cout<<endl;
	}
	fclose(stdin);
	fclose(stdout);
}
