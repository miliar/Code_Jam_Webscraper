#include <iostream>

using namespace std;

string popPlus(string s) {
	string resultString = s;
	while(!resultString.empty()) {
		char last = resultString.back();
		if (last == '+')
		{
				resultString.pop_back();
		}
		else {
			break;
		}
	}
	return resultString;
}

string flipString(string s) {
	string resultString, curString = s;
	while(!curString.empty()) {
		char last = curString.back();
		char push = (last == '+') ? '-' : '+';
		resultString.push_back(push);
		curString.pop_back();
	}
	return resultString;
}

int main() {

	int T;
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
			string S, curString;
			int count = 0;
			cin >> S;
			curString = popPlus(S);

			while(!curString.empty()) {

				int index = 0;
				while(curString.at(index) == '+') {
					curString.at(index) = '-';
					index++;
				}
				if (index > 0)
				{
						count++;
				}
				curString = flipString(curString);
				curString = popPlus(curString);
				count++;
			}

			cout << "Case #" << i + 1 << ": " << count << endl;

	}

	return 0;
}