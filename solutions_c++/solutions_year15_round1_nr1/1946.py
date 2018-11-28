#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <cctype>
using namespace std;

long long int solve_problem_a( vector<int> input){
	long long int num_eaten = 0;
	
	for(int i =1; i < input.size() ; i++){
		int diff = input[i-1] - input[i];
		if(diff > 0){
			num_eaten += diff;
		}
	}

	return num_eaten;
}

long long int solve_problem_b(vector<int> input){
	long long int num_eaten = 0;
	
	long long int min_dec = 0;

	for(int i =1; i < input.size() ; i++){
		int diff = input[i-1] - input[i];
		if(diff > 0){
			if(diff > min_dec){
				min_dec = diff;
			}
		}
	}

	for(int i = 1; i<input.size(); i++){
		int diff = input[i-1] - input[i];
		if(input[i-1] < min_dec){
			num_eaten += input[i-1];
		}
		else{
			num_eaten += min_dec;
		}
	}
	//num_eaten = min_dec*(input.size()-1);
	return num_eaten;

}

int main(){
  int case_num = 0;

	cin >> case_num;

	for(int n =0; n < case_num; n++){
		int case_size = 0;
		cin >> case_size;
		
		vector<int> input;
		input.resize(case_size);

		for(int j = 0; j< input.size(); j++){
			int temp;
			cin >> temp;
			input[j] = temp;						
		}
		cout << " Case #" << n+1 << ": " << solve_problem_a(input) << " "
				 << solve_problem_b(input)<< endl;
	}
}
