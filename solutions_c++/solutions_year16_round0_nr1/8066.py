#include<iostream>
using namespace std;

int find_digs(long long int num, int dig[]){
	int d;
	while(num){
		d=num%10;
		num/=10;
		dig[d]=1;
	}
	for(int i=0; i<10;i++){
		if(dig[i]==0)
			return 0;
	}
	return 1;
}

int main(){
	int t;
	long long int n,j;	
	cin>>t;
	for(int i=1; i<=t; i++){
		cin>>n;
		if(n==0){
			cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
			continue;
		}
		int dig[10]={0};
		long long int mult;
		j=1;
		while(1){
			mult=n*j;
			if(find_digs(mult,dig)){
				cout<<"Case #"<<i<<": "<<mult<<endl;
				break;
			}
			j++;
		}
	}
	return 0; 
}