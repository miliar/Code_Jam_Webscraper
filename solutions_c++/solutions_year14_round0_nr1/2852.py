#include<iostream>
#include<fstream>
using namespace std;

int main(){
	int a1[4][4];
	int a2[4][4];
	ofstream myfile;
	myfile.open ("output.txt");
	int t,i,j,m,n,count,c,k=0;
	cin>>t;
	while(t--){
		cin>>m;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				cin>>a1[i][j];
			}
		}
		cin>>n;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				cin>>a2[i][j];
			}
		}
		m=m-1;
		n=n-1;
		count=0;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				if(a1[m][i]==a2[n][j]){
					count++;
					c=a1[m][i];
				}
			}
		}
		k++;
		if(count==1){
			myfile<<"Case #"<<k<<": "<<c<<endl;
		}
		else if(count>1){
			myfile<<"Case #"<<k<<": "<<"Bad magician!"<<endl;
		}
		else{
			myfile<<"Case #"<<k<<": "<<"Volunteer cheated!"<<endl;
		}
	}
	
	return 0;
}
