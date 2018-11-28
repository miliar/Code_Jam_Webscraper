#include<iostream>
using namespace std;

bool check(int a[][100],int a1,int x1,int x2,int n,int m){
	bool var1=true;
	bool var2=true;
	for (int i=0;i<m;i++){
		//cout<<a[x1][i]<<endl;
		var1= (var1 && (a1>=a[x1][i]));
		if (var1==false) break;
	}
	for (int i=0;i<n;i++){
		//cout<<a[i][x2]<<endl;
		var2= (var2 && (a1>=a[i][x2]));
		if (var2==false) break;
	}
	return (var1 || var2);
}
	
		
int main(){
	int t;
	int n;
	int m;
	int size[100][100];
	cin>>t;
	int k=0;
	while(k<t){
	cin>>n;
	cin>>m;
	for (int i=0;i<n;i++){
		for (int j=0; j<m;j++)
		{
			cin>>size[i][j];
		}
	}
	int check1=true;
	for(int i=0;i<n;i++){
		for (int j=0;j<m;j++){
			check1= check1 && (check(size,size[i][j],i,j,n,m));
			if (check1==false) break;
		}
		if (check1==false) break;
	}
	if (check1) cout<<"Case #"<<k+1<<": "<<"YES"<<endl;
	else cout<<"Case #"<<k+1<<": "<<"NO"<<endl;
	k++;
}
}
	
	
