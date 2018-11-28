#include <iostream>
#include <string>

using namespace std;

string flip(string str, int end)
{
	string res = str;
	string test = "";
	string test2 = "";
	for(int i=0; i<str.length(); i++)
	{
		test+='-';
		test2+='+';
	}
	if(str.compare(test) == 0)
	{
		return test2;
	}
	
	for(int i=0; i<=end; i++)
	{
		if(str[end-i] == '-')
			res[i] = '+';
		else if(str[end-i] == '+')
			res[i] = '-';
	}

	return res;
}

int pancake(string str)
{
	int count = 0;
	size_t index = 0;
	string res="";
	for(int i=0; i<str.length(); i++)
	{
		res+='+';
	}
	while(str.compare(res))
	{
		if(str[0] == '-')
		{
			index = str.find_first_of('+') -1;
		}
		else if(str[0] == '+')
		{
			index = str.find_first_of('-') -1;
		}
		str = flip(str, index);
		count++;
	}

	return count;
}

int main()
{
	int T, N;
	cin >> T;
	for(int i=0; i<T; i++)
	{
		string str;
		cin >> str;

		cout << "Case #" << i+1 << ": " << pancake(str) << endl;
	}

	return 0;
}
