#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
using namespace std;

bool isSleep(int arr[]){
	//cout << endl;
	for(int i=0;i<10;i++){
		//cout << i << ": "<<arr[i] << "    "; 
		if(arr[i] == 0){
			return false;
		}
	}
	return true;
}

int main(){
	int ttCase;
	cin >> ttCase;
	int curr = 1;
	unsigned long long currNum;
	int countArr[10];
	while(ttCase --){
		memset(countArr,0,sizeof(countArr));
		cin >> currNum;
		unsigned long long num;
		cout << "Case #" << curr << ": ";
		//cout << "\ncurrNum: "<<currNum <<"\n";
		for(int i=1;i<=10000;i++){
			num = currNum*i;


			if((num == currNum*(i+1)) && (i != 10)){
				cout << "INSOMNIA";
				break;
			}

			else{
				while (num != 0){
					int digit = num%10;

					num = num/10;
					countArr[digit]++;
					//cout << " d: "<< digit << " countArr[d]: " << countArr[digit];
				}
			}
			//
			//cout << num <<" "<<isSleep(countArr);
			//
			if(isSleep(countArr)){
				cout << currNum*i;
				break;
			}
		}
		curr++;
		cout << endl;
	}
}
