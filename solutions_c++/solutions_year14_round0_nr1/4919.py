#include<iostream>
using namespace std;

void putin(int *a);

int main(){
	int a[4];
	int b[4];
	int i,j;
	int flag,result;
	int t,k;
	cin>>t;
	for(k=1;k<=t;k++){
		flag=0;
		putin(a);
		putin(b);
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				if(a[i]==b[j]){
					flag++;
					result=a[i];
				}
			}
		}
		if(flag==1)cout<<"Case #"<<k<<": "<<result<<endl;
		else if(flag==0)cout<<"Case #"<<k<<": "<<"Volunteer cheated!"<<endl;
		else cout<<"Case #"<<k<<": "<<"Bad magician!"<<endl;
	}
}

void putin(int *a){
	int n,i,j;
	int temp;
	cin>>n;
	n--;
	for(i=0;i<4;i++){
		if(i==n){
			for(j=0;j<4;j++)cin>>a[j];
		}
		else{
			for(j=0;j<4;j++)cin>>temp;
		}
	}
}