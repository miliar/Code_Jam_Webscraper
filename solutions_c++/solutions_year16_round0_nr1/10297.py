#include<iostream>
using namespace std;
int main(){
	int t,n,ar[10];
	cin>>t;
	cout<<"T is "<<t<<endl;
	for(int i=0;i<t;i++){
		for(int p=0;p<10;p++)
			ar[p]=0;
		cout<<"I is "<<i+1<<endl;
	
		int cn=0;
		cin>>n;
		if(n==0){
			cout<<"Case #"<<(i+1)<<": "<<"INSOMNIA"<<endl;
			continue;
		}
		for(int j=1;cn!=10;j++){
			cout<<"Enter here."<<endl;
			int num=n*j;
			cout<<"Num is: -"<<num;
			int temp=num;
			while(temp>0){
				int rem=temp%10;
				cout<<"Rem is: -"<<rem<<ar[rem-1]<<endl;
			
				if(ar[rem-1]==0){
					ar[rem-1]++;
					cn++;
					cout<<"counted "<<rem<<endl;
				}
				temp=temp/10;
			}
			if(cn==10){
				cout<<"Case #"<<(i+1)<<": "<<num<<endl;
				break;
			}
		}
		cout<<i+1<<"...........\n";
		
	}
}

