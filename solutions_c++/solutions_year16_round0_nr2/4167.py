#include <iostream>
#include <string>
using namespace std;

int main()
{
	int T;
	int index = 1;
	cin >> T;

	while(T--){
		string str;
		cin >> str;
		int len = str.length();
		int count = 0;
		int start = 0;
		for (int i=len-1;i>=0;i--){
			if (str[i]=='+')
				continue;
			else{
				start = i;
				break;
			}
		}
		if (start == 0){
			if (str[start] == '-') count = 1;
			cout << "Case #" << index++ << ": " << count << endl;
			continue;
		}
		count = 1;
		char curr = '-';
		while(start>=0){
			if (str[start]==curr){
				start--;
			}
			else{
				curr = str[start];
				start--;
				count++;
			}
		}
		cout << "Case #" << index++ << ": " << count << endl;
	}
	return 0;
}