#include <iostream>
using namespace std;

int main(void)
{
	int T;
	cin >> T;

	for(int t = 1; t <= T; t++)
	{
		string input, output;
		cin >> input;

		char l = input[0];
		for(int i = 0; i < input.length(); i++){
			if(input[i] >= l){
				output = input[i] + output;
				l = input[i];
			}
			else{
				output += input[i];
			}

//			cout<<output<<endl;
		}



		cout << "Case #" << t << ": " << output << endl;
	}
}