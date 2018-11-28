#include <iostream>
#include <string>
#include <stdlib.h>

using namespace std;

unsigned long long power(int x, unsigned int y)
{
	unsigned long long temp;
	if (y == 0)
		return 1;
	temp = power(x, y / 2);
	if (y % 2 == 0)
		return temp*temp;
	else
		return x*temp*temp;
}

unsigned long long getBaseRes(string str, int base)
{
	unsigned long long value = 0;
	for (int i = str.length() - 1, j = 0; i >= 0; i--, j++)
	{
		if (str[i] == '1')
		{
			value += power(base, j);
		}
	}
	return value;
}
bool isPrime(unsigned long long data, unsigned long &multiplier){
	bool flag = true;
	multiplier = 1;
	for (unsigned long long i = 2; i <= sqrt(data); ++i)
	{
		if (data%i == 0)
		{
			flag = false;
			multiplier = i;
			break;
		}
	}
	return flag;
}

bool IsJam(string data){
	unsigned long proofdataArr[9] = { 0 };
	bool flag = true;
	unsigned long multiplierValue = 1;
	for (size_t i = 0, base = 2; i < 9; i++, base++)
	{
		unsigned long long ConvertbaseData = getBaseRes(data, base);
		if (!isPrime(ConvertbaseData, multiplierValue)){
			proofdataArr[i] = multiplierValue;
		}
		else{
			flag = false;
			break;
		}
	}

	if (flag){
		cout << data;
		for (size_t i = 0; i < 9; i++){
			cout << " " << proofdataArr[i];
		}
		cout << endl;
	}
	return flag;
}

void SetArray(char* buff, int index)
{
	buff[index] = '1';
}

string convertIntToBinaryString(unsigned long long intVal, int N)
{
	char *binaryChar = (char *)malloc(sizeof(char) * (N + 1));
	memset(binaryChar, '0', N + 1);
	for (int i = N - 1; intVal > 0; i--)
	{
		if (intVal % 2 == 0)
			binaryChar[i] = '0';
		else
			binaryChar[i] = '1';
		intVal /= 2;
	}
	binaryChar[N] = '\0';
	string strRet(binaryChar);
	free(binaryChar);
	return strRet;
}

int main()
{
	int iTestCases = 0, N, J;
	cin >> iTestCases;
	for (int i = 1; i <= iTestCases; i++)
	{
		cin >> N >> J;
		cout << "Case #" << iTestCases <<":"<< endl;
		char *buff = new char[N + 1];
		buff[N] = '\0';
		memset(buff, '0', N);

		SetArray(buff, 0);
		SetArray(buff, N - 1);

		unsigned long long minRange = getBaseRes(buff, 2);

		for (int k = 1; k < N - 1; k++){
			SetArray(buff, k);
		}
		unsigned long long maxRange = getBaseRes(buff, 2);

		int distinct = 0;
		while (distinct < J && minRange < maxRange)
		{
			string testString = convertIntToBinaryString(minRange, N);
			if (testString[0] != '0' && testString[N - 1] != '0' && IsJam(testString))
				distinct++;
			minRange++;
		}

		delete(buff);
	}
	return 0;
}