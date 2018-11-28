/* Google Code Jam #1 
Utsav Ahuja @ University of Southern California
*/ 

#include <iostream>


using namespace std;


void readLists(int*, int);
void printList(std::ostream& ofile);
int calculate(bool* nums, int n);
void resetNums(bool* nums);

int main(int argc, char* argv[]){
	int cases;
	cin >> cases;
	int* testCases = new int[cases];
	readLists(testCases, cases); 
	bool nums[10];
	for(int i = 0; i < cases; i++){
		resetNums(nums);
		int result = calculate(nums, testCases[i]);
		cout << "Case #" << i+1 << ": ";
		if(result == -1) cout << "INSOMNIA" << endl;
		else cout << result << endl;

	}
}

int calculate(bool* nums, int n){
	if(n == 0) return -1;
		
	else{
		int numLeft = 10;
		int multiple = n;
		int digit;
		while(numLeft > 0){
			int temp = multiple;
			while(temp > 0){
				digit = temp % 10;
				if(!nums[digit]){
					nums[digit] = 1;
					numLeft--;
				}
				temp /= 10;
			}
			multiple += n;
		}
		return multiple-n;
	}
}


void resetNums(bool* nums){
	for(int i = 0; i < 10; i++){
		nums[i] = 0;
	}
}

void readLists(int* input, int cases){
	int temp;
	for(int i = 0; i < cases; i++){
		cin >> temp;
		input[i] = temp;
	}
}

void printList(std::ostream& ofile){
}

