#include <bits/stdc++.h>
using namespace std;
unordered_multiset<char> charSet;
multiset <int> phoneNum;
int main ()
{
	int t;
	string str;
	cin >> t;
	for (int z=1; z<=t; ++z)
	{
		cin >> str;
		charSet.clear();
		phoneNum.clear();
		for (char c: str)
		{
			charSet.insert(c);
		}
		while (charSet.find('Z') != charSet.end())
		{
			charSet.erase(charSet.find('Z'));
			charSet.erase(charSet.find('E'));
			charSet.erase(charSet.find('R'));
			charSet.erase(charSet.find('O'));
			
			phoneNum.insert(0);
		}
		while (charSet.find('W') != charSet.end())
		{
			charSet.erase(charSet.find('T'));
			charSet.erase(charSet.find('W'));
			charSet.erase(charSet.find('O'));
			
			phoneNum.insert(2);
		}
		while (charSet.find('U') != charSet.end())
		{
			charSet.erase(charSet.find('F'));
			charSet.erase(charSet.find('O'));
			charSet.erase(charSet.find('U'));
			charSet.erase(charSet.find('R'));			
			
			phoneNum.insert(4);
		}
		while (charSet.find('X') != charSet.end())
		{
			charSet.erase(charSet.find('S'));
			charSet.erase(charSet.find('I'));
			charSet.erase(charSet.find('X'));
			
			phoneNum.insert(6);
		}
		while (charSet.find('G') != charSet.end())
		{
			charSet.erase(charSet.find('E'));
			charSet.erase(charSet.find('I'));
			charSet.erase(charSet.find('G'));
			charSet.erase(charSet.find('H'));
			charSet.erase(charSet.find('T'));
			phoneNum.insert(8);
		}
		while (charSet.find('O') != charSet.end())
		{
			charSet.erase(charSet.find('O'));
			charSet.erase(charSet.find('N'));
			charSet.erase(charSet.find('E'));
			
			phoneNum.insert(1);
		}
		while (charSet.find('T') != charSet.end())
		{
			charSet.erase(charSet.find('T'));
			charSet.erase(charSet.find('H'));
			charSet.erase(charSet.find('R'));
			charSet.erase(charSet.find('E'));
			charSet.erase(charSet.find('E'));
			
			phoneNum.insert(3);
		}
		while (charSet.find('F') != charSet.end())
		{
			charSet.erase(charSet.find('F'));
			charSet.erase(charSet.find('I'));
			charSet.erase(charSet.find('V'));
			charSet.erase(charSet.find('E'));			
			
			phoneNum.insert(5);
		}
		while (charSet.find('S') != charSet.end())
		{
			charSet.erase(charSet.find('S'));
			charSet.erase(charSet.find('E'));
			charSet.erase(charSet.find('V'));
			charSet.erase(charSet.find('E'));
			charSet.erase(charSet.find('N'));
			
			phoneNum.insert(7);
		}
		while (charSet.find('N') != charSet.end())
		{
			charSet.erase(charSet.find('N'));
			charSet.erase(charSet.find('I'));
			charSet.erase(charSet.find('N'));
			charSet.erase(charSet.find('E'));
			phoneNum.insert(9);
		}
		
		
		cout << "Case #" << z << ": ";
		for (int t: phoneNum)
		{
			cout << t;
		}
		cout << endl;
	}
	return 0;
}

