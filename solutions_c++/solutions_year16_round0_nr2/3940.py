#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;

int main ()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);

	int TC;
	cin >> TC;
	int CC = 1;
	while (TC--)
	{
		string s;
		cin >> s;
		s += '+';
		int cnt=0;
		for (int i=0 ; i<s.size()-1 ; i++)
		{
			if (s[i] != s[i+1]) cnt++;
		}
		printf("Case #%d: %d\n",CC++,cnt);
	}
}