#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>

using namespace std;

string decode(string stack)
{
	int i;
	string res = "";
	char p = 0;
	
	for(i=0;i<stack.length();i++)
	{
		if(stack[i] == p) continue;
		else
		{
			p = stack[i];
			res += stack[i];
		}
	}
	return res;
}

int main()
{
	int t, i;
	
	cin >> t;	
	for (i=0;i<t;i++)
	{
		string n;
		cin >> n;
		string s = decode (n);
		if(s.length() == 1 && s[0] == '+')
		{
			cout << "Case #" << i+1 << ": " << 0 << endl;
		}
		else if(s.length() == 1 && s[0] == '-')
		{
			cout << "Case #" << i+1 << ": " << 1 << endl;
		}
		else if( (s.length()%2 == 0 && s[0] == '-') || (s.length()%2 == 1 && s[0] == '+') )
		{
			cout << "Case #" << i+1 << ": " << s.length() - 1  << endl;
		}
		else
		{
			cout << "Case #" << i+1 << ": " << s.length() << endl;
		}
	}
}
