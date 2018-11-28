#include <iostream>
#include <string>
using namespace std;


inline void flip(string & input, string::iterator & input_itr, unsigned int len){

	string text_to_flip = input.substr(0, len);
	for(string::reverse_iterator it_rbegin = text_to_flip.rbegin(), it_rend = text_to_flip.rend(); it_rbegin != it_rend; it_rbegin++){
		char & c = *it_rbegin;
		*input_itr = (c == '-') ? '+' : '-';
		input_itr++;
	}

}

int main(){

	int no_of_tests;
	cin >> no_of_tests;

	int test_index = 0;

	//cannot call getline immediatelly after cin. 	
	char c = cin.peek();
	if(c == '\n'){ cin.ignore(1, '\n'); }
	else if(c ==  '\r'){ cin.ignore(1, '\r'); }

	string input;
	while(test_index++ < no_of_tests){
		getline(cin, input);

		unsigned int temp_index;
		int count =0;

		while(true){

			string::iterator input_itr = input.begin();
				
			if (*input_itr == '-'){
				temp_index = input.find_last_of("-");
				//flip all to the left including itself
				flip(input, input_itr, temp_index + 1);
			}
			else{
				temp_index = input.find_first_of('-');
				if(temp_index == string::npos){
					break;
				}
				flip(input, input_itr, temp_index);			
			}
			count++;
		};

		cout<< "Case #" << test_index <<": " << count <<endl;
	}
}