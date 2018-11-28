#include<iostream>
using namespace std;
int main(){
	int t, m, n, count,e;
	int a[4][4], b[4][4];
	cin>>t;
	for(int k=1;k<=t;k++){
		count=0;
		cin>>m;
		m--;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++)
				cin>>a[i][j];
		}
		cin>>n;
		n--;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++)
				cin>>b[i][j];
		}
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(a[m][i]==b[n][j]){
					count++;
					e=a[m][i];
					break;
				}	
			}
		}
		cout<<"Case #"<<k<<": ";
		if(count==0)
			cout<<"Volunteer cheated!\n";
		else if(count>1)cout<<"Bad magician!\n";
		else cout<<e<<endl;
		
	}
}
