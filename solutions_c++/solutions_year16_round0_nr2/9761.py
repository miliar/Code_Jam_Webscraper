#include <iostream>
#include <string>
 
using namespace std;

void reverse(int temp){
	if(temp == 0) temp = 1;
	else temp = 0;
}

int check(int arr[], int len, int count){ 

	int pos=-1;
	int i;

	for(i=0; i<len; i++){
		if(arr[i] == 0) pos = i;		
	}

	if(pos == -1) return count;
	else{
		for(i=0; i<=pos; i++){
			if(arr[i] == 0) arr[i] = 1;
			else arr[i] = 0;
		}
		count++;
		return check(arr, len, count);
	}
}

int main(){

	int t;
	string pan;
	int arr[100];
	int len;
	int count;

	cin >> t;
	int i,j=0,res;
	while(j<t){
		cin >> pan;
		len = pan.size();

		count = 0;
		for(i=0; i<len; i++){
			if(pan[i] == '+') arr[i] = 1;
			else arr[i] = 0;
		}
		
		res = check(arr, len, count);
		cout << "Case #" << j+1 << ": " << res <<endl;
		j++;
	}

	return 0;
}
