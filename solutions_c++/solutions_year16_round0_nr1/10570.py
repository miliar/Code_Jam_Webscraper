#include<iostream>
using namespace std;
main(){
	int t,x,count;
	long n;
	long long num,i,j,temp;
	cin>>t;
	for(i=1;i<=t;i++){
		int a[10]={0};
		cin>>n;
		if(n==0){
			cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
		}
		else{
			count=0;
			num=0;
			for(j=0;;j++){
				temp=n*j;
				while(temp>0){
					x=temp%10;
					if(a[x]!=1){
						a[x]=1;
						count++;
					}
					temp/=10;
				}
				if(count==10){
					num=n*j;
					break;
				}
			}
			cout<<"Case #"<<i<<": "<<num<<endl;
		}
		
	}
}