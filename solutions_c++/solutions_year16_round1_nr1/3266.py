#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <stdint.h>

using namespace std;

int main()
{
	int t;
	
	cin >> t;
	for (int j = 1; j <= t; j++){
		string s, answer = "";
		cin >> s;
		answer += s[0];
		for (int i = 1; i < s.length(); i++){
			//	cout << s[i] << ' ' << answer[0] << ' ' << answer[answer.length() - 1] << endl;
			if (s[i] >= answer[answer.length() - 1])
				answer = answer + s[i];
			else answer = s[i] + answer;

		}
		cout << "Case #" << j << ": ";
		for (int i = answer.length() - 1; i >= 0; i--)
			cout<<answer[i];
		cout << endl;
	}
	//cout << ("A" > "C"); true
	//	system("pause");
	return 0;
}