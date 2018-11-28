#include <iostream>
#include <string>
#include <vector>

using namespace std;

void readinput(vector<int>& input){
	int size, next;
	cin>>size;
	for (int i=0; i<size; i++){
		cin>>next;
		input.push_back(next);
	}
}

int checkvector(vector<int>& output){
	int sum=0;	
	for (int i=0; i<output.size(); i++){
		sum = sum + output[i];
	}
	return sum;
}

int calculate(vector<int>& output, int input){
	int k=0, m=200, result;
	if (input==0)
		return 0;
	
	while (checkvector(output)!=45){
		k = k+1;
		m = input * k;
		while (m>=10){
			if (output[m%10]==-1)
				output[m%10] = m%10;	
			m = m/10;
		}
		if (m<10){
			if (output[m]==-1)
				output[m] = m;
		}
	}
	result = input * k;
	return result;
}

int main(){
	int answer;
	vector<int> input;
	vector<int> output(10, -1);
	readinput(input);
	for (int i=0; i<input.size(); i++){
		output.assign(10, -1);
		answer = calculate(output, input[i]);
		if (answer==0){
			cout << "Case #" << i+1 << ": ";
			cout << "INSOMNIA" << endl;
		}
		else{
			cout << "Case #" << i+1 << ": ";
			cout << answer << endl;
		}
	}

	return 0;
	
}
