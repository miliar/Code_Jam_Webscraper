#include<iostream>
#include<fstream>
using namespace std;

int a[4][4];
int b[4][4];
int p=0;
ofstream myfile;

int func(int n, int m){
	n=n-1;
	m=m-1;
	int i,j,count=0,k;
	for(i=0;i<4;i++){
		for(j=0;j<4;j++){
			if(a[n][i]==b[m][j]){
				count++;
				k=a[n][i];
			}
		}
	}
	//cout<<count<<endl;;
	if(count==1){
		myfile<<"Case #"<<p<<": "<<k<<endl;
	}
	else if(count>1){
		myfile<<"Case #"<<p<<": "<<"Bad magician!"<<endl;
	}
	else{
		myfile<<"Case #"<<p<<": "<<"Volunteer cheated!"<<endl;
	}
}

int main(){
	int t,n,m,i,j;
	cin>>t;
	myfile.open ("output.txt");
	p=0;
	while(t--){
		p++;
		cin>>n;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				cin>>a[i][j];
			}
		}
		cin>>m;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				cin>>b[i][j];
			}
		}
		func(n,m);
	}
	return 0;
}
