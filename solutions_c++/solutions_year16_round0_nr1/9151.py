#include <iostream>
using namespace std;

void fill(int arr[], long n){
	while(n){
		int a=n%10;
		n=n/10;
		arr[a]=1;
	}
	
}

bool check(int arr[]){
	for(int i=0;i<10;i++){
		if(arr[i]==0) return false;
	}
	return true;
}


int main() {
	// your code goes here
	long k;
	cin>>k;
	for(long t=1;t<=k;t++){
		long n;
		cin>>n;
		cout<<"Case #"<<t<<": ";
		if(n==0){
			cout<<"INSOMNIA"<<endl;
			continue;
		}
		int arr[10];
		for(int i=0;i<10;i++) arr[i]=0;
		long i=1;
		while(!check(arr)){
			fill(arr,i*n);
			i++;
		}
		cout<<(i-1)*n<<endl;
	}
	return 0;
}