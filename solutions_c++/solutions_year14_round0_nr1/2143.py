#include<iostream>
#include<cstdio>
using namespace std;

int main(){
	freopen("ip.txt","r",stdin);
	freopen("op1.txt","w",stdout);
	int t,k=1;
	cin>>t;
	while(t--){
		int row,a[17];
		for(int i=1;i<17;i++) a[i]=0;
		cin>>row;
		for(int i=1;i<=4;i++)
		for(int j=1;j<=4;j++){
			int x;
			cin>>x;
			if(i==row)
				a[x]++;
		}
		cin>>row;
		for(int i=1;i<=4;i++)
		for(int j=1;j<=4;j++){
			int x;
			cin>>x;
			if(i==row)
				a[x]++;
		}
		int c=0,num;
		for(int i=1;i<=16;i++)
			if(a[i]>1){ c++;num=i;}
		if(c==1) cout<<"Case #"<<k<<": "<<num<<endl;
		else if(c==0) cout<<"Case #"<<k<<": Volunteer cheated!"<<endl;
		else cout<<"Case #"<<k<<": Bad magician!"<<endl;
		k++;
	}
	return 0;
}
