#include<iostream>

using namespace std;

long long int Answer1;
long long int Answer2;
long long int N;
long long int arr[1000];

int main(){
	int T;
	cin >> T;
	for(int test_case=0; test_case<T; test_case++){
		//input
		cin >> N;
		for(int i=0; i<N; i++){
			cin >> arr[i];
		}
		
		Answer1 = 0;
		Answer2 = 0;
		//algo
		long long int temp = arr[0];
		for(int i=1; i<N; i++){
			if(arr[i] >= temp){
				temp = arr[i];
			} else {
				Answer1 = Answer1 + temp - arr[i];
				temp = arr[i];
			}
		}
		temp = 0;
		int i = N;
		while(i > 1){
			if(arr[i-1] < arr[i-2]){
				if(temp < (arr[i-2] - arr[i-1])){
					temp = arr[i-2] - arr[i-1];
				}
			}
			i--;
		}
		for(i=0; i<N-1; i++){
			if(arr[i] < temp){
				Answer2 = Answer2 + arr[i];
			} else {
				Answer2 = Answer2 + temp;
			}
		}
		
		//output
		cout << "Case #" << test_case+1 << ": " << Answer1 << " " << Answer2 << endl;
		
	}
	return 0;
}
