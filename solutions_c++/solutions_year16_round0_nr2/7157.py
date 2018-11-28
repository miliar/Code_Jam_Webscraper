/* Google Code Jam #1 
Utsav Ahuja @ University of Southern California
*/ 

#include <iostream>


using namespace std;


void readLists(int**, int);

int calculate(int* nums, int n, int);
void flip(int* nums, int divide);


int main(int argc, char* argv[]){
	int cases;
	cin >> cases;
	int** testCases = new int*[cases];
	for(int i = 0; i < cases; i++){
		testCases[i] = new int[101]; //+ = true, - = false
	}

	readLists(testCases, cases); 

	for(int i = 0; i < cases; i++){
		int result = calculate(testCases[i], testCases[i][0], 0);
		cout << "Case #" << i+1 << ": ";
		cout << result << endl;
	}
}

int calculate(int* nums, int n, int sum){
	if(n == 0) return sum;
	
	for(int i = n; i >= 0; i--){
		if(nums[i] == 0){
			flip(nums, i);
			return calculate(nums, i, ++sum);
		}
	}	
	return sum;	
}

void flip(int* nums, int divide){
	for(int i = 1; i <= divide; i++){
		if(nums[i] == 1) nums[i] = 0;
		else nums[i] = 1;
	}
}



void readLists(int** input, int cases){
	string temp;
	for(int i = 0; i < cases; i++){
		cin >> temp;
		input[i][0] = temp.length();
		for(int j = 1; j <= temp.length()+1; j++){
			if(temp[j-1] == '+')
				input[i][j] = 1;
			else input[i][j] = 0;	
		}
	}
}


