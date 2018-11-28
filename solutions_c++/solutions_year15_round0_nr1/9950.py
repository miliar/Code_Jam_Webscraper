
#include<iostream>
using namespace std;
int main(){
	int t,n;
	cin>>t;
	for(int l = 0; l < t; l++){
		cin>>n;
		char arr[n+1];
		cin>>arr;
		int friends = 0;
		int sum = arr[0]-'0';
		for(int i = 1; i <=n; i++){
			
			if( i > sum){
				friends += i - sum;
				sum = i;
			}
			sum += arr[i] - '0';
			
		}
		cout<< "Case #"<<l+1<<": "<<friends<<endl;
	}
}
