#include <iostream>

#include <climits>
#include <vector>
#include <cstring>

typedef long long vlong;
typedef long long unsigned uvlong;

#define LOL(x) cout << #x <<" = " <<endl  

using namespace std;


void func(){
	string party[26] = {"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"};
	int arr[26];
	int P;
	cin >>  P;
	int sum=0;int max=0;
	for(int i=0;i<P;i++){
		cin >> arr[i];
		if(arr[i] > max){
			max = i;
		}
		sum += arr[i];
	}
	int i =0;
	int count  = 0;

	for(int j=1;j<P;j++){
		for(int m=j;m > 0;m--){
			if(arr[m] > arr[m-1]){
				int temp = arr[m];
				arr[m]= arr[m-1];
				arr[m-1] = temp;
				string te = party[m];
				party[m] = party[m-1];
				party[m-1] = te;
			}
			else
				break;
		}
	}

	while(sum > 0) {
		if(count == 2 || sum == 2){
			count = 0;
			cout <<" ";
		}

			cout << party[0];
			arr[0] -=1;
			
			for(int j=1;j<P;j++){
				for(int m=j;m > 0;m--){
					if(arr[m] > arr[m-1]){
						int temp = arr[m];
						arr[m]= arr[m-1];
						arr[m-1] = temp;
						string te = party[m];
						party[m] = party[m-1];
						party[m-1] = te;
					}
					else
						break;
				}
			}
			count++;	
		sum--;
	}
}


int main(){

	int T;
	cin >> T;
	for(int i=0;i<T;i++){

		cout <<"Case #" << i+1 <<": "; func(); cout << endl;
	}

}
