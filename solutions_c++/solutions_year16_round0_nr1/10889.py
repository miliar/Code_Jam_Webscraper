#include<iostream>
using namespace std;


int main(){
	
	int t, n;
	cin >> t;
	
	for(int i=1; i<=t; i++){
		cin >> n;
		
		int arr[10] = {0};
		int count = 0;
		
		if (n == 0){
			cout<< "Case #"<<i<<": INSOMNIA\n";
		}
		else{
			int j = 0;
			while(1){
				int num = j*n;
			
				while(num){
					if(arr[num%10] == 0){
						arr[num%10]++;
						count++;
					}
			
					num = num / 10;
				}
		
				if(count == 10){
					break;
				}
				j++;
			}
			cout << "Case #"<<i<<": "<<n*j<<"\n";
		}
	}
	
	return 0;
}