#include <iostream>
#include <string.h>

using namespace std;

int main()
{
	int t;
	cin >> t;
	int q = 1;
	while(q <= t) {

		string str;
		cin >> str;

		string result = "";
		result += str[0];
		for(int i = 1; i < str.length(); ++i) {
			if(str[i] >= result[0])
				result = str[i] + result;
			else
				result += str[i];
		}

		cout << "Case #" << q << ": " << result << endl;

		q++;
	}

	return 0;
}