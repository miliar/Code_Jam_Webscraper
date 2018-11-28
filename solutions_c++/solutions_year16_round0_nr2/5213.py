#include <iostream>

using namespace std;

int main()
{
	int test = 0;
	cin >> test;
	for (int t = 1; t <=test; ++t){
		string input;
		cin >> input;
		input += '+';
		int i = -1, current_index = 0;
		int result = 0;
		for (current_index = 0 ; current_index < input.size(); 
			++current_index){
			if (input.at(current_index) == '+'){
				if (current_index - i > 1){
					if (i != -1)
						result +=2;
					else 
						++result;
				}
				i = current_index;
			}
		}
		cout << "Case #" << t << ": " << result << endl;
	}
	return 0;
}
