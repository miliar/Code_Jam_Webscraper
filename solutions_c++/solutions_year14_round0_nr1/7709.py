#include<iostream>
using namespace std;

int main(){
	int t;
	cin>>t;
	for(int cnt=1;cnt<=t;cnt++){
		
		int a,temp;
		int f[]={0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
		cin>>a;
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++){
				cin>>temp;
				if(i==a)f[temp]=1;
			}
		cin>>a;
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++){
				cin>>temp;
				if(i==a)f[temp]+=1;
			}
		temp=0;
		for(int i=1;i<=16;i++)if(f[i]==2){temp++;a=i;}
		cout<<"Case #"<<cnt<<": ";
		if(temp==0)cout<<"Volunteer cheated!\n";
		else if(temp==1)cout<<a<<"\n";
		else cout<<"Bad magician!\n";
	}
}