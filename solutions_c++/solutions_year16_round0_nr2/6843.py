#include <iostream>
#include <string>

using namespace std;

void reverse(string &s, int n)
{
	string r = s;
	for(int i=0; i<n; i++)
	{
		if(r[i] == '+') s[n-i-1] = '-';
		else s[n-i-1] = '+';
	}
}

void solve(string &s)
{
	
}

int main(int argc, char *argv[])
{
    int test;
	cin >> test;
	for(int t=0; t<test; t++)
	{
		string s;
		cin >> s;
		int steps = 0;
		for(int i=s.length()-1; i>=0; i--)
		{
			if(s[i] == '+') continue;
			if(s[0] == '-')
			{
				reverse(s, i+1);
				steps++;
				continue;
			}
			int p;
			for(int j=i-1; j>=0; j--)
			{
				if(s[j] == '+')
				{
					p = j;
					break;
				}
			}
			reverse(s, p+1);
			steps++;
			reverse(s, i+1);
			steps++;
		}
		cout << "Case #" << t+1 << ": " << steps << endl;
	}
    return 0;
}
