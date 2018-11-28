#include <iostream>

using namespace std;
int main(){
	int n,k;
	int arr[10];
	int temp,mul,cnt;

	cin>>n;
	for(int i=0;i<n;i++){
		cin>>k;

		if(k==0)
			cout<<"Case #"<<(i+1)<<": "<<"INSOMNIA"<<endl;
		else{
			for(int j=0;j<10;j++){
				arr[j]=0;
			}
			cnt=0;

			mul=0;
			while(cnt!=10){
				mul++;
				temp=k*mul;

				while(temp){
					if(!arr[temp%10]){
						arr[temp%10]=1;
						cnt++;
					}

					temp=temp/10;
				}
			}

			cout<<"Case #"<<(i+1)<<": "<<mul*k<<endl;
		}
	}
}