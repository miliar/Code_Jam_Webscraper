#include <iostream>
using namespace std;
 
int main() {
	int t,a;
	cin>>t;
	for(a=1;a<=t;a++){
 	long long int n;	
	cin>>n;
	if(n==0){
			cout<<"Case #"<<a<<": "<<"INSOMNIA"<<endl;
			continue;
	}
	long long int c[10]={};
	long long int m=1,flag=0,temp,i;
	while (flag==0){
		temp=n*m;
		while(temp!=0){
			c[temp%10]++;
			temp=temp/10;
		}
		for(i=0;i<10;i++){
			if(c[i]==0){
				flag=0;
				break;
			}
			else{
				flag=1;
			}
		}
	m++;
	}
	cout<<"Case #"<<a<<": "<<n*(m-1)<<endl;
	}
	return 0;
}