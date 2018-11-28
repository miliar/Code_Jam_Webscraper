#include <iostream>
#include <algorithm>
#include <stdio.h>

using namespace std;

int main(){
	int test;
	cin >> test;
	for(int k = 1; k <= test; k++){
		int hash[10] = {0};
		int temp[10] = {0};
		long long int num,temp_num;
		cin >> num;
		temp_num = num;
		int j = 1;
		if(num == 0){
			cout <<"Case #"<<k<<": INSOMNIA"<<"\n";
		}
		else{
			while(true){
				//cout << j << " " <<num <<"\n";
				while(true){
					int a = num % 10;
					//cout <<  a << "\n";
					hash[a] = 1;
					num = num / 10;
					if(num == 0){
						break;
					}
				}
				num = temp_num;
				int count = 0;
				for(int i = 0;i < 10;i++){
					if(hash[i] == 1){
						count++;
					}
				}
				if(count == 10){
					break;
				}
				j++;
				num = j*num;
			}
		cout <<"Case #"<<k<<": "<<num*j<<"\n";
	}
	}
}