#include <iostream>
#include <vector>
#include <sstream>
#include <string>
#include <algorithm>

using namespace std;

vector<char> numbers;
int start = 0;

int count(int c)
{
	if(c == 0) return -1;
	else
	{
		bool found = false;
		stringstream a;
		a << c;
		string check = a.str();
		int len = check.length();

		for(int i = 0; i < len; ++i)
		{
			found = false;
			int sz = numbers.size();
			char letter = check.at(i);
			for(int j = 0; j < sz; ++j)
			{
				if(numbers.at(j) == letter)
					found = true;
			}
			if(!found)
				numbers.push_back(letter);
		}
		if(numbers.size() == 10)
		{
			return c;
		}
		else
		{
			return count(c + start);
		}
	}
}

int main(){

	int T;
	int answer;
	cin >> T;
	for(int i = 0; i < T; ++i)
	{
		while (!numbers.empty())
		{
            numbers.pop_back();
		}
		cin >> start;
		answer = count(start);
		cout << "Case #" << i+1 << ": ";
		if(answer < 0)
			cout << "INSOMNIA" << endl;
		else
			cout << answer << endl;
	}

    return 0;
}
