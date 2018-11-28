#include<cstdio>
#include<string>
#include<iostream>
#include<algorithm>

using namespace std;

string str;

int find()
{
	for(int i = str.size()-1; i >= 0; i--)
	{
		if(str[i] == '-')
			return i;
	}
	return -1;
}

void change(int idx)
{
	for(int i = 0; i <= idx; i++)
	{
		if(str[i] == '+')	str[i] = '-';
		else	str[i] = '+';
	}
}

int main()
{
	int tcc;
	scanf("%d", &tcc);
	for(int i = 1; i <= tcc; i++)
	{
		cin >> str;

		int last_idx = find();

		int result = 0;
		while(last_idx != -1)
		{
			change(last_idx);
			last_idx = find();
			result++;
		}
		printf("Case #%d: %d\n", i, result);
	}
}
