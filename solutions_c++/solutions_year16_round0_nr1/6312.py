#include <iostream>
using namespace std;

int main(){
	long long int T,N,C;
	cin>>T;
	for(int t=1;t<=T;t++){
		cin>>N;
		if (N==0) {
			cout<<"Case #"<<t<<": INSOMNIA"<<"\n";
			continue;
		}
		int arr[10]={0,0,0,0,0,0,0,0,0,0};
		C=1;
		long long int n;
		lab:n=N*(C);
		while(n!=0){
			arr[n%10]=1;
			n=n/10;
		}
		if(arr[0]&&arr[1]&&arr[2]&&arr[3]&&arr[4]&&arr[5]&&arr[6]&&arr[7]&&arr[8]&&arr[9]) {
			cout<<"Case #"<<t<<": "<<C*N<<"\n";
			continue;
		}
		else{
			C++; goto lab;
		}
	}	
	return 0;
}