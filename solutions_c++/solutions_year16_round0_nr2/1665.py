#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int count_flips (string s)
{
	reverse(s.begin(),s.end());
	int count=0;
	char curr=s[0];
	if (curr=='+')
		count=0;
	else
		count=1;
	
	for (int i=1; i<s.length(); i++)
	{
		if (s[i]!=curr)
		{
			count++;
			curr=s[i];
		}
	}
	return count;
}

int main() {
	int t;
	cin >> t;
	for (int i=0; i<t; i++)
	{
		string s;
		cin >> s;
		int answer = count_flips(s);
		printf ("Case #%d: %d\n", i+1, answer);
	}
}
