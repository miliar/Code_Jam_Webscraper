#include <iostream>
#include <cstdio>

using namespace std;
int str[26];
int num[10];
void countstring(char* s)
{
	int i = 0;
	for (int a = 0; a < 26; a++)
	{
		str[a] = 0;
	}
	for (int a = 0; a < 10; a++)
	{
		num[a] = 0;
	}
	while (s[i] != '\0')
	{
		str[(s[i] - 'A')]++;
		i++;
	}
}
void decrease(int a)
{
	bool done = false;
	while (!done)
	{
		switch (a)
		{
		case 0:
			if (str['Z' - 'A'])
			{
				num[0]++;
				str['Z' - 'A']--; str['E' - 'A']--; str['R' - 'A']--; str['O' - 'A']--;
			}
			else{
				done = true;
			}
			break;
		case 1:
			if (str['O' - 'A'])
			{
				num[1]++;
				str['O' - 'A']--; str['N' - 'A']--; str['E' - 'A']--;
			}
			else
			{
				done = true;
			}
			break;
		case 2:
			if (str['W' - 'A'])
			{
				num[2]++;
				str['T' - 'A']--; str['W' - 'A']--; str['O' - 'A']--;
			}
			else
			{
				done = true;
			}
			break;
		case 3:
			if (str['R' - 'A'])
			{
				num[3]++;
				str['T' - 'A']--; str['H' - 'A']--; str['R' - 'A']--; str['E' - 'A']--; str['E' - 'A']--;
			}
			else
			{
				done = true;
			}
			break;
		case 4:
			if (str['F' - 'A'])
			{
				num[4]++;
				str['F' - 'A']--; str['O' - 'A']--; str['U' - 'A']--; str['R' - 'A']--; 
			}
			else
			{
				done = true;
			}
			break;
		case 5:
			if (str['V' - 'A'])
			{
				num[5]++;
				str['F' - 'A']--; str['I' - 'A']--; str['V' - 'A']--; str['E' - 'A']--; 
			}
			else
			{
				done = true;
			}
			break;
		case 6:
			if (str['X' - 'A'])
			{
				num[6]++;
				str['S' - 'A']--; str['I' - 'A']--; str['X' - 'A']--;
			}
			else
			{
				done = true;
			}
			break;
		case 7:
			if (str['S' - 'A'])
			{
				num[7]++;
				str['S' - 'A']--; str['E' - 'A']--; str['V' - 'A']--; str['E' - 'A']--; str['N' - 'A']--;
			}
			else
			{
				done = true;
			}
			break;
		case 8:
			if (str['G' - 'A'])
			{
				num[8]++;
				str['E' - 'A']--; str['I' - 'A']--; str['G' - 'A']--; str['H' - 'A']--; str['T' - 'A']--;
			}
			else
			{
				done = true;
			}
			break;
		case 9:
			if (str['N' - 'A'])
			{
				num[9]++;
				str['N' - 'A']--; str['I' - 'A']--; str['N' - 'A']--; str['E' - 'A']--; 
			}
			else
			{
				done = true;
			}
			break;

		}
	}
	
}
int main(void)
{
	freopen("A.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		char s[2002];
		scanf("%s", s);
		countstring(s);
		decrease(0);
		decrease(2);
		decrease(6);
		decrease(8);
		decrease(7);
		decrease(5);
		decrease(4);
		decrease(3);
		decrease(1);
		decrease(9);
		char ans[2000]; int cnt = 0;
		for (int i = 0; i < 10; i++)
		{
			for (int j = 0; j < num[i]; j++)
			{
				ans[cnt++] = ('0' + i);
			}
		}
		ans[cnt] = '\0';
		printf("Case #%d: %s\n", t, ans);
	}
	
	return 0;
}

