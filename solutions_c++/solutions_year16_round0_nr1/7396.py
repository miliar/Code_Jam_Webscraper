#include <iostream>
#include <string>
#include <vector>

using namespace std;
int function(long num,int arr[]) {
	int rem;
	while(num!=0) {
		rem = num%10;
		arr[rem]++;
		num/=10;
	}
	for(int j=0;j<10;j++) {
		if(arr[j]==0) {
			return 0;
		}
	}
	return 1;
}
int main() {
	int i;
	cin>>i;
	int joker = 1;
	while(joker<=i) {
		long number;
		int flag =0;
		cin>>number;
		long temp;
		int a[10] ={0};
		int k=1;
		if(number==0) {
				cout<< "Case #"<<joker<<": "<<"INSOMNIA"<<endl;
			}
		else {
		while(1) {

				temp = number*k;
				int isit = function(temp,a);
				if(isit) {
					cout<< "Case #"<<joker<<": "<<temp<<endl;
					break;
				}
				k++;
			}
		}
		++joker;
	}
	return 0;
}