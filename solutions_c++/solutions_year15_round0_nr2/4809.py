#include <iostream>
#include <fstream>

using namespace std;

int ans;

void recursion(int arr[], int count, int m){
	if(count == 0){
		ans = min(ans, m);
		return;
	}

	int maximum = 0, index, zero, temp, arr1[100];
	int one[10], two[10];
	bool flag = false;
	for(int i=0 ; i<10 ; i++){
		one[i] = two[i] = 0;
	}

	for(int i=0 ; i<100 ; i++){
		arr1[i] = arr[i];
		one[arr[i]]++;
	}

	for(int i=0 ; i<100 ; i++){
		if(arr[i]>maximum){
			maximum = arr[i];
			index = i;
		}
	}

	for(int i=0 ; i<100 ; i++){
		if(arr[i] == 0){
			zero = i;
			break;
		}
	}

	if(maximum != 9){
		temp = maximum / 2;
		arr1[zero] = temp;
		arr1[index] -= temp;
	} else {
		temp = 3;
		arr1[zero] = 3;
		arr1[index] = 6;
	}

	for(int i=0 ; i<100 ; i++){
		two[arr1[i]]++;
	}

	for(int i=0 ; i<10 ; i++){
		if(one[i] != two[i]){
			flag = true;
			break;
		}
	}

	if(flag){
		recursion(arr1, count, m+1);
	}

	arr1[zero] = 0;
	arr1[index] += temp;

	for(int i=0 ; i<100 ; i++){
		if(arr1[i]>0){
			arr1[i]--;
			count--;
		}
	}

	recursion(arr1, count, m+1);
}

int main(){
	ofstream output;
	ifstream input;

	output.open("out.txt");
	input.open("in.txt");

	int t, l=1;
	input>>t;

	while(t--){
		int d, temp = 0;
		input>>d;

		int arr[100];
		for(int i=0 ; i<100 ; i++)
			arr[i] = 0;

		for(int i=0 ; i<d ; i++){
			input>>arr[i];
			temp += arr[i];
		}

		ans = 1000;

		recursion(arr, temp, 0);

		output<<"Case #"<<l++<<": ";
		output<<ans<<endl;
	}

	return 0;
}