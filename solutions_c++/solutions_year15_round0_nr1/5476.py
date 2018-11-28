#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <cctype>
using namespace std;

int solve_problem( vector<int> input){
  long long int extra_members = 0;
	long long int total_members = 0;
	for(int i =0; i< input.size(); i++){

		if( input[i] != 0 ){
			if(total_members <= i){
				extra_members += i - total_members;
				total_members += input[i] + extra_members;
			}
			else{
				total_members += input[i];
			}
		}
	}

	return extra_members;
}

int main(){
  int case_num = 0;

	cin >> case_num;

	for(int i =0; i < case_num; i++){
		int case_size = 0;
		cin >> case_size;
		
		vector<int> input;
		input.resize(case_size+1);
		string temp;
		cin >> temp;
	//	cout << temp << endl;
		for(int j = 0; j< input.size(); j++){ 
			input[j] = temp[j] - '0';
	//		cout << input[j] << " ";
		}
	//	cout << endl;

		cout << " Case #" << i+1 << ": " << solve_problem(input) << endl;
	}
}
