#if 1
#include<iostream>
#include<string>
using namespace std;

FILE* pF;
FILE* pAnsF;
string cake;

int process(string s)
{
	int Answer = 0;
	if (s[0] == '-')
	{
		Answer++;
	}
	for (unsigned i = 1; i < s.size(); i++)
	{
		if (s[i] == '-')
		{
			Answer = Answer + 2;
		}
	}
	return Answer;
}
string compressCake(string source)
{
	string cstr;
	int pos=0;
	cstr.push_back(source[0]);
	for (unsigned i = 1; i < source.size(); i++)
	{
		if (source[i] != cstr[pos])
		{
			cstr.push_back(source[i]);
			pos++;
		}
	}
	return cstr;
}
int main()
{
	freopen_s(&pF, "Text.txt", "r", stdin);
	freopen_s(&pAnsF, "OutputCakeLarge.txt", "w", stdout);

	int C;

	cin >> C;

	for (int c = 1; c <= C; c++)
	{
		
		cin >> cake;
	
		string str = compressCake(cake);

		int Answer = process(str);
		
		cout << "Case #" << c << ": " << Answer << endl;
		
	}

	return 0;
}
#endif