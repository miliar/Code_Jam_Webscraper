#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

bool checkString(const string& s)
{
	for(int i = 0; i<s.size(); i++)
	{
		if(s[i] == '-')
		{
			return false;
		}
	}
	return true;
}

void strrev(string& s)
{
	for(int i = 0; i<s.size()/2; i++)
	{
		char temp = s[i];
		s[i] = s[s.size()-i - 1];
		s[s.size()-i - 1] = temp;
	}
}

void toggleChar(string&s, int i)
{
	//toggles ith character
	if( s[i] == '+')
	{
		s[i] = '-';
	}
	else
	{
		s[i] = '+';
	}
}

void flip(string& s)
{
	//flips and toggles string s
	for(int i = 0; i<s.size(); i++)
	{
		toggleChar(s, i);
	}
	strrev(s);
}

int minMoves(string& s)
{
	if(s.size() == 1)
	{
		if(checkString(s) == false)
		{
			return 1;
		}
		return 0;
	}
	int moves = 0;
	string remString;
	for(int i = 0; i<s.size()-1 && checkString(s) != true ; i++)
	{
		/*if(s[i] == s.size() -1)
		{
			break;
		}*/
		if(s[i]!= s[i+1])
		{
			remString = s.substr(i+1);
			string temp = s.substr(0,i+1);
			flip(temp);
			s = temp + remString;
			moves++;
		}
	}
	if(checkString(s)!= true)
	{
        return moves + 1;
	}
	return moves;
}

int main()
{
	int T;
	cin>>T;
	string* inputStrings = new string[T];
	for(int i = 0; i<T; i++)
	{
		cin>>inputStrings[i];
	}
	for(int j = 0; j<T; j++)
	{
		cout<<"Case #"<<j+1<<": ";
		cout<<minMoves(inputStrings[j])<<endl;
	}
	delete [] inputStrings;
}