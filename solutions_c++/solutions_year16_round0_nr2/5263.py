#include<iostream>
using namespace std;

int main()
{
	int testCases;
	cin >> testCases;
	for (int  j = 0 ; j < testCases; j++)
	{
		string s;
		cin >> s;
		int length = s.length(), i = length-1;
		while (i >= 0 && s[i] == '+')
			i--;
		if (i == -1)
		{
			cout << "Case #" << j+1 << ": 0" << endl;
			continue;
		}
		
		s = s.substr(0, i+1);
		//cout << s<< endl;
		i = 1;
		length = s.length();
		int count = 1;
		while (i < length)
		{
			while (i < length && s[i] == s[i-1])
				i++;
			if (i == length)
				break;
			count++;
			i++;		
		}
		cout << "Case #" << j+1 << ": "<< count << endl;
	}
}
