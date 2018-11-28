#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
//#define _CRT_SECURE_NO_WARNINGS
using namespace std;

long long ch2d( char ch)
{
	return ch - '0';
}
char d2ch(long long d)
{
	return d + '0';
}

long long getEachMax( string digit)
{
	long long n00 = atoi(digit.c_str());
	int Len = digit.length();
	//if (digit[Len-1]=='0')
	//{
	//	for (int i = Len / 2; i >= 0; i--)
	//	{
	//		if (digit[i] != '0' && i!=0)
	//		{
	//			digit[i] =  char(digit[i] - 1);
	//			break;
	//		}
	//		if (digit[i] > '1' && i == 0)
	//		{
	//			digit[i] = max('1', char(digit[i] - 1));
	//			break;
	//		}
	//	}
	//}
	if (digit[Len - 1] == '0')
	{
		string strTmp = string(digit.begin(), digit.begin() + Len / 2 + 1);
		long long longTmp = atoi(strTmp.c_str());
		longTmp--;

		for (int i = Len / 2; i >= 0; --i)
		{
			digit[i] = d2ch(longTmp % 10);
			longTmp /= 10;
		}
		if (digit[0]=='0')
		{
			return 0;
		}
	}
	if (Len <= 1)
	{
		return 0;
	}
	for (int i = 0; i < Len / 2; ++i)
	{
		digit[Len - 1 - i] = '0';
	}
	digit[Len - 1] = '1';
	long long n0 = atoi(digit.c_str());
	if (n0>n00)
	{
		return 0;
	}
	string digit_reverse = digit;
	reverse(digit_reverse.begin(), digit_reverse.end());
	if (digit_reverse == digit)
		return 0;
	long long n1 = atoi(digit_reverse.c_str());
	return n1 - n0 + 1;
}

char chs[20];
long long solve(string digit)
{
	long long ret = 0;
	int Len = digit.length();
	for (int i = 0; i < Len - 1; ++i)
	{
		chs[i] = '9';
		chs[i + 1] = '\0';
		string str = string(chs);
		long long tmp = getEachMax( str);
		ret += tmp;
	}
	ret += getEachMax(digit);
	return ret;
}
int main()
{
	freopen("A-small-attempt2.in", "r", stdin);
	//freopen("sample.txt", "r", stdin);


	int N;
	cin >> N;

	FILE * p; p = fopen("result.txt", "w");
	
	for (int i = 0; i < N; ++i)
	{
		string data;
		cin >> data;
		long long needSkip = solve(data);
		long long ret = atoi(data.c_str()) + needSkip;
		fprintf(p, "Case #%d: %d\n", i + 1, ret);
	}
	fclose(p);
	return 0;
}