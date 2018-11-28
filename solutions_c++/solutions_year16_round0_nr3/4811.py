#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<vector>
#include<string>

using namespace std;

typedef long long i64;

i64 divisor(i64 num)
{
	i64 pivot = (i64)round(sqrt(num));
	for (i64 i = 2; i <= pivot; ++i)
	{
		if (num % i == 0)
			return i;
	}
	return 0;
}

i64 make_num(int base, string str)
{
	i64 num = 0;
	for (int i = str.size() - 1; i >= 0; --i)
	{
		if(str[i] == '1')
			num += (i64)pow(base, str.size() - 1 - i);
	}
	return num;
}

string next_num(string str)
{
	for (int i = str.size() - 2; i > 0; --i)
	{
		if (str[i] == '0')
		{
			str[i] = '1';
			for (int j = i + 1; j < str.size() - 2; ++j)
				str[j] = '0';
			return str;
		}
	}
	return "";
}

int main(void)
{
	//scanf("%d\n");
	freopen("output.txt", "w", stdout);
	int N = 16;
	int J = 50;
	int count = 0;
	string s_num = "1000000000000001";
	i64 divs[9];
	printf("Case #1: \n");
	while (count < J)
	{
		bool drop = false;
		for (int i = 2; i < 11; ++i)
		{
			i64 div = divisor(make_num(i, s_num));
			if (div)
			{
				divs[i - 2] = div;
			}
			else
			{
				drop = true;
				break;
			}
		}

		if (!drop){
			count++;
			cout << s_num;
			for (int i = 0; i < 9; i++)
			{
				cout << " " << divs[i];
			}
			cout << "\n";
		}
		s_num = next_num(s_num);
	}
	return 0;
}