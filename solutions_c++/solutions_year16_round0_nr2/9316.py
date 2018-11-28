#include <iostream>
#include <string>
using namespace std;

typedef unsigned long long ui;

int main(){

	ui T = 0;
	cin >> T;
	ui N = 0;
	ui case_num = 1;

	while(T--){

		string input_string;
		cin >> input_string;

		ui len = input_string.size();
		int flag = 0;
		ui num_ops = 0;
		for(ui index=0; index<len; index++){
			if(input_string[index]=='-' && flag == 0){
				if(index==0){
					num_ops += 1;
				}
				else{
					num_ops += 2;
				}
				flag = 1;
			}
			else if(input_string[index]=='+'){
				flag = 0;
			}
		}
		cout << "Case #" << case_num << ": " << num_ops << endl;
		case_num++;
	}

	return 0;
}