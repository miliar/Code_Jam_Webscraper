#include<iostream>
#include<cstring>

using namespace std;

bool check(int arr[]){
	for(int i=0;i<10;i++){
		if(arr[i]==0){
			return false;
		}
	}
	return true;
}

int main(){
	long long temp2,t,n,temp,ans;
	cin>>t;
	for(int i=1;i<=t;i++){
		cin>>n;
		temp=n;
		if(n==0){
			cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
		}
		else{
		  int arr[10];
		  memset(arr,0,sizeof(arr));
		  while(true){
		  	if(check(arr)){
		  		break;
		  	}
		  	temp2=n;
		  	while(n){
		  		arr[n%10]=1;
		  		n=n/10;
		  	}
		  	n=temp2;
		  	n=n+temp;
		  }

		  cout<<"Case #"<<i<<": "<<temp2<<endl;

		}


	}

}