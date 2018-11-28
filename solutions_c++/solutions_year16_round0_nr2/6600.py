#include <iostream>

using namespace std;

bool string_has_all_happy(const string& s) {
	return s.find_first_not_of('+') == std::string::npos;
}

int main() {
	int T;
	int count,pos,pos2;
	string stack;
	
	cin >> T;
	for(int i = 0; i < T; i++) {
		cin >> stack;
		count = 0;
		pos2 = 0;
		cout << "Case #" << i+1 << ": ";
		while(!string_has_all_happy(stack)) {
			pos = pos2;
			count++;
			//cout << "STACK: " << stack << endl;
			//cout << "Length: " << stack.length() << endl;
			//cout << "here" << endl;
			
			if(stack[0] == '+') {
				while(stack[pos] == '+')
					pos++;
				while(stack[pos] == '-' && pos < stack.length())
					pos++;
			}
			else {
				while(stack[pos]=='-' && pos < stack.length()) {
					//cout << "stuck" << endl;
					pos++;
				}
			}
			//cout << "POS: " << pos << endl;
			for(int j = 0; j < pos; j++) {
				if(stack[j]=='+')
					stack[j]='-';
				else
					stack[j]='+';
			}
		}
		
		/*if(string_has_all_happy(stack))
			cout << "All good" << endl;*/
		
		
		cout << count << endl;
		//cout << stack << endl;
	}

}