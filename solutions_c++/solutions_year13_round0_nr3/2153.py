#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>
#include <list>
#include <stack>
#include <algorithm>
#include <queue>
#include <map>
#include <cstdlib>
#include <set>
#include <string>
#include <cstring>
#include <memory>
using namespace std;

//ofstream fout("C:\\Users\\Administrator\\Desktop\\C.out");
#define fout cout

class C
{
public:
	void Run();

private:
	void Input();
	void Do();
	void Output();
	bool IsIt(int num[], int length);
	int Mul(int num[], int length, int dis[]);
	void DisplayN(int num[], int length);
	long long Convert(int num[], int length);

private:
	int caseNum, caseIndex;
	int numBuffer[200];
	long long low, high;
	int count;
};

void C::Run()
{
	scanf("%d", &caseNum);
	for(caseIndex = 1; caseIndex <= caseNum; ++caseIndex)
	{
		Input();
		Do();
		Output();
	}
}

void C::Input()
{
	scanf("%lld %lld", &low, &high);
}

void C::Do()
{
	count = 0;
	long long low2 = (long long)sqrt((double)low);
	while(low2 * low2 < low) ++low2;
	long long high2 = (long long)sqrt((double)high);
	while(high2 * high2 <= high) ++high2;

	long long low3 = (long long)pow(10.0, double((long long)(log((double)low2) / log(10.0)) >> 1));
	long long high3 = (long long)pow(10.0, double((((long long)(log((double)high2) / log(10.0))) >> 1) + 1));
	for(long long base = low3; base <= high3; ++base)
	{
		if(base % 10 == 0) continue;

		int num1[100];
		int l1 = 0;
		long long tmp = base;
		bool isOK = true;
		while(tmp)
		{
			num1[l1++] = tmp % 10;
			tmp /= 10;
			if(num1[l1 - 1] > 2) { isOK = false; break; }
		}
		if(!isOK) continue;

		int num2[100];
		int l2 = l1 << 1;
		for(int i = 0; i < l1; ++i)
		{
			num2[l2 - 1 - i] = num1[i];
		}
		for(int i = l1 - 1; i >= 0; --i)
		{
			num2[i] = num1[i];
		}

		tmp = Convert(num2, l2);
		if(tmp >= low2 && tmp < high2)
		{
			memset(numBuffer, 0, sizeof(numBuffer));
			int l3 = Mul(num2, l2, numBuffer);
			if(IsIt(numBuffer, l3)) ++count;
		}

		l2 = (l1 << 1) - 1;
		for(int i = 0; i < l1 - 1; ++i)
		{
			num2[l2 - 1 - i] = num1[i];
		}
		for(int i = l1 - 1; i >= 0; --i)
		{
			num2[i] = num1[i];
		}

		tmp = Convert(num2, l2);
		if(tmp >= high2) break;
		if(tmp >= low2)
		{
			memset(numBuffer, 0, sizeof(numBuffer));
			int l3 = Mul(num2, l2, numBuffer);

			if(IsIt(numBuffer, l3)) ++count;
		}
	}

	if( 9 >= low && 9 <= high) ++count;
}

bool C::IsIt(int num[], int length)
{
	int len = length >> 1;
	for(int i = 0; i < len; ++i)
		if(num[i] != num[length - 1 - i]) return false;
	return true;
}

long long C::Convert(int num[], int length)
{
	long long n = 0;
	for(int i = length - 1; i >= 0; --i)
	{
		n *= 10;
		n += num[i];
	}
	return n;
}

int C::Mul(int num[], int length, int dis[])
{
	int len = 0;
	for(int i = 0; i < length; ++i)
	{
		int add = 0;
		for(int j = 0; j < length; ++j)
		{
			dis[i + j] += add + num[i] * num[j];
			add = dis[i + j] / 10;
			dis[i + j] %= 10;
		}
		len = i + length;
		while(add)
		{
			dis[len++] += add % 10;
			add /= 10;
		}
	}
	while(dis[len - 1] == 0) --len;
	return len;
}

void C::DisplayN(int num[], int length)
{
	for(int i = length - 1; i >= 0; --i)
		fout << num[i];
}

void C::Output()
{
	fout << "Case #" << caseIndex << ": " << count << endl;
	//printf("Case #%d: %s\n", caseIndex, result ? "YES" : "NO");
}

C instance;
int main()
{
	instance.Run();
	return 0;
}
