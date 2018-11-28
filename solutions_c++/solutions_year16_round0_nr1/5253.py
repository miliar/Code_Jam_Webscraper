#include <bits/stdc++.h>

using namespace std;

bool checkAll(int arr [],int size){
	for(int i = 0 ; i < size; i ++){
		if(arr[i] == 0){
			return false;
		}
	}
	return true;
}

int main(){

	int t;
	unsigned long long n;
	cin >> t;
	for(int j = 1; j <= t ; j++){
		cin >> n;
		if( n == 0){
			cout<<"Case #"<<j<<": INSOMNIA"<<endl;
			continue;
		}
		unsigned long long count = 1;
		int digits[10] = {0,0,0,0,0,0,0,0,0,0};
		while(true){
			unsigned long long next = n*count;
			while(next != 0){
				int pos = next % 10;
				digits[pos] = 1;
				next = next/10;
			}

			if(checkAll(digits,10)){
				cout<<"Case #"<<j<<": "<<n*count<<endl;
				break;
			}
			count++;
		}
	}
}