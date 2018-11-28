#include<iostream>
using namespace std;

bool arr[10];


bool checkDigits(long long int n){
int temp;
	while(n>0){	
	temp = n%10;
	arr[temp]=1;
	n/=10;		
	}
for(int i=0;i<10;i++)if(arr[i]==0)return false;
return true;		
}

int main(){
long long int n;
int t=0,k=1,j=1;
cin>>t;
while(t--){
for(int i=0;i<10;i++)arr[i]=0;
j=1;	
cin>>n;
	if(n==0)cout<<"Case #"<<k++<<": INSOMNIA"<<endl;
	else{
		while(!checkDigits(n*j++));	
		cout<<"Case #"<<k++<<": "<<n*(j-1)<<endl;
	}
}
return 0;
}

