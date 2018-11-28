#include <iostream>

using namespace std;

int countflip(string input)
{
	int count = 0;
	int len = input.length();
	if(len == 0) return 0;
	if(len == 1) return 0;
	for(int i = 0; i < len-1; ++i)
	{
		if(input.at(i) != input.at(i+1))
			++count;
	}
    return count;
}

int main()
{
	int T;
	cin >> T;
	for(int i = 0; i < T; ++i)
	{
	    string input;
	    cin >> input;
		int answer = countflip(input);
		int sz = input.length();
		char bottom = input.at(sz-1);
        cout << "Case #" << i+1 << ": ";
		if(bottom == '-')
			cout << answer + 1 << endl;
		else
			cout << answer << endl;
	}

	return 0;
}
