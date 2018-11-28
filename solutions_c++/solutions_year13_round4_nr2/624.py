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

#pragma comment(linker, "/STACK:104857600,104857600")

using namespace std;

#define FILE_IO

class B
{
public:
	void Run();

private:
	void Input();
	void Do();
	void Output();
	void Join(int x, int y, int x0, int y0);
	void GetHead(int x, int y, int &x0, int &y0);

private:
	static const int MAX_SIZE = 500;
	int caseNum, caseIndex;
	int n;
	long long rank;
	long long p;
	int a, b;
};

void B::Run()
{
	scanf("%d", &caseNum);
	for(caseIndex = 1; caseIndex <= caseNum; ++caseIndex)
	{
		Input();
		Do();
		Output();
	}
}

void B::Input()
{
	scanf("%d %lld", &n, &p);
}

void B::Do()
{
	rank = 0LL;
	for(int i = n - 1; i >= 0; --i)
	{
		rank <<= 1;
		long long tmp = (long long)(1LL) << i;
		if(p > tmp)
		{
			rank += 1;
			p -= tmp;
		}
		else
		{
			rank += 0;
		}
	}

	for(int i = ((1 << n) - 1); i >= 0; --i)
	{
		long long tmpRank = 0LL;
		int stronger = i;
		for(int j = n - 1; j >= 0; --j)
		{
			tmpRank <<= 1;
			if(stronger)
			{
				stronger = (stronger - 1) / 2;
				tmpRank += 1;
			}
		}
		if(tmpRank <= rank)
		{
			a = i;
			break;
		}
	}
	for(int i = ((1 << n) - 1); i >= 0; --i)
	{
		long long tmpRank = 0LL;
		int weak = (1 << n) - 1 - i;
		for(int j = n - 1; j >= 0; --j)
		{
			tmpRank <<= 1;
			if(weak)
			{
				weak = (weak - 1) / 2;
			}
			else
			{
				tmpRank += 1;
			}
		}
		if(tmpRank <= rank)
		{
			b = i;
			break;
		}
	}
}

void B::Output()
{
	printf("Case #%d: %d %d", caseIndex, a, b);
	printf("\n");
}

B instance;
int main()
{
	#ifdef FILE_IO
	freopen("C:\\Users\\Administrator\\Desktop\\data\\in.txt", "r", stdin);
	freopen("C:\\Users\\Administrator\\Desktop\\data\\out.txt", "w", stdout);
	#endif

	instance.Run();
	return 0;
}
