#include <iostream>
using namespace std;
void flip(string &str, int start_index, int end_index){
	for (int i = start_index; i <= end_index; ++i)
	{
		if (str[i] == '+')
			str[i] = '-';
		else if (str[i] == '-')
			str[i] = '+';
	}
}
int main(){
	int test_cases;
	cin >> test_cases;
	int temp = test_cases;
	while(test_cases--){
		string str;
		cin >> str;
		int length = str.length();
		int steps = 0;
		for (int i = length-1; i >= 0 ; )
		{
			if ( str[i] == '+' )
				i--;
			else if ( str[i] == '-' ){
				flip(str, 0, i);
				steps++;
				i--;
			}
		}
		cout << "Case #" << temp-test_cases << ": " << steps << endl;

	}

	return 0;
}