#include<iostream>
using namespace std;
int main(){
	int t;
	cin>>t;
	for(int k=1;k<=t;k++){
		int x,y,m;
		int a[4][4],b[4][4];
		int c=0;
		cin>>x;
		for(int i=1;i<=4;i++){
			for(int j=1;j<=4;j++){
				cin>>a[i][j];
			}
		}
		cin>>y;
		for(int i=1;i<=4;i++){
			for(int j=1;j<=4;j++){
				cin>>b[i][j];
			}
		}
		for(int i=1;i<=4;i++){
			for(int j=1;j<=4;j++){
				if(a[x][i]==b[y][j]){
					m=a[x][i];
					c++;
				}
			}
		}
		//cout<<c<<endl;
		cout<<"Case #"<<k<<": ";
		if(c==1){
			cout<<m <<endl;
		}
		if(c==0){
			cout<<"Volunteer cheated!"<<endl;
		}
		else if(c!=1 && c!=0){
			cout<<"Bad magician!"<<endl;
		}
	}
}
