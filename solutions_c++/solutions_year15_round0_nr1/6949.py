#include <iostream>
#include <string>

using namespace std;

int T;
int max;
string s;


int num(char c) 
{
	return c - 48;
}


void do_case(int num_case) 
{
	int clap = 0;
	int count = 0;
	for (int i = 0; i < s.length(); ++i) 
	{
		if (i > clap) 
		{
			count += i - clap;
			clap += i - clap;
		}
		clap += num(s[i]);
	}
	printf("Case #%d: %d\n", num_case, count);
}

int main() 
{
	cin >> T;

	for (int i = 0; i < T; i++) 
	{
		cin >> max;
		cin >> s;
		do_case(i+1);
	}

	return 0;
}