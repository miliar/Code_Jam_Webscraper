#include <iostream>
#include <string>
#include <vector>

using namespace std;

void readinput(vector<string>& input){
	int number;
	string str;
	cin>>number;
	for (int i=0; i<number; i++){
		cin>>str;
		input.push_back(str);
	}
}

int check_succession(string input){
	int i=0;
	int k=1;
	while (input.substr(i,1)==input.substr(i+1, 1)){
		i=i+1;
		k++;	
	}
	return k;
}

string flip_it(string input, int succession){	
	for (int i=0; i<succession; i++){
		if (input.substr(i, 1) == "+"){
			input[i] = '-';
		}
		else input[i]= '+';	
	}
	return input;
}

string allplusorminus(string input){
	bool allplus = true;
	bool allnegative = true;
	for (int i=0; i<input.length(); i++){
		if (input.substr(i, 1) == "+"){
			allnegative = false;
		}
		else{
			allplus = false;
		}
	}
	if (allnegative==false && allplus==false)
		return "neither";
	else if (allnegative==true)
		return "minus";
	else
		return "plus"; 
}

int main(){
	int succession =0;
	vector<string> input;
	readinput(input);
	for (int i=0; i<input.size(); i++){
		int count =0;
		while (allplusorminus(input[i])=="neither"){
			succession = check_succession(input[i]);
			input[i] = flip_it(input[i], succession);
			count = count+1;
		}
		if (allplusorminus(input[i]) == "minus") count++;
		cout << "Case #" << i+1 << ": " << count << endl;
	}
	return 0;
}
