#include<istream>
#include<iostream>
#include<string>
using namespace std;

int main()
{
	int cases; cin >> cases;
	int ncase = 1;
	string stack;
	for (int i = 0; i < cases; i++)
	{
		cin >> stack;
		int length = stack.length();
		int moves = 0;
		for (int i = 0; i < length-1; i++)
		{
			if (stack[i] != stack[i + 1])
				moves++;
		}
		if (stack[length - 1] == '-')
			moves++;
		cout << "Case #" << ncase++ << ": " << moves << endl;
	}
}
