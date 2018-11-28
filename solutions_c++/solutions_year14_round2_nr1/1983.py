#include <cstdio>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int T;
int N;

string s1, s2;
int num = 0;

void do_case(int index)
{
	cin >> N;
	s1 = "";
	s2 = "";
	num = 0;

	getline(cin, s1);
	getline(cin, s1);
	getline(cin, s2);

	int i1 = 0;
	int i2 = 0;

	while (i1 < s1.length() && i2 < s2.length())
	{
		if (s1[i1] != s2[i2])
		{
			printf("Case #%d: FEGLA WON\n", index + 1);
			return;
		}

		while (i1 + 1 < s1.length() && s1[i1 + 1] == s1[i1] && i2 + 1  < s2.length() && s2[i2+1] == s2[i2])
		{
			i1++;
			i2++;
		}


		while (i1 + 1 < s1.length() && s1[i1 + 1] == s1[i1])
		{
			i1++;
			num++;
		}
		while (i2 + 1  < s2.length() && s2[i2 + 1] == s2[i2])
		{
			i2++;
			num++;
		}

		i1++;
		i2++;
	}

	if (num == 0 &&  s1.length() != s2.length() || i1 != s1.length() || i2 != s2.length())
		printf("Case #%d: FEGLA WON\n", index + 1);
	else
		printf("Case #%d: %d\n", index + 1, num);
}

int main()
{
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
		do_case(i);
	}

	return 0;
}