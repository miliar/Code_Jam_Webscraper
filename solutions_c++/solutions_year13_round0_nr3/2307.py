#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

char Tmp[100];

int isP(long long X)
{
	sprintf(Tmp, "%I64d", X);
	int Len = strlen(Tmp);
	for (int i = 0; i < Len; i ++)
		if (Tmp[i] != Tmp[Len - 1 - i])
			return 0;
	return 1;
}

char Tmp2[100];

long long Kuo1(long long X)
{
	sprintf(Tmp, "%I64d", X);
	int Len = strlen(Tmp);
	int Ptr = 0;
	for (int i = 0; i < Len; i ++)
		Tmp2[Ptr ++] = Tmp[i];
	for (int i = Len - 2; i >= 0; i --)
		Tmp2[Ptr ++] = Tmp[i];
	Tmp2[Ptr] = 0;
	long long Ret = 0;
	sscanf(Tmp2, "%I64d", &Ret);
	return Ret;
}

long long Kuo2(long long X)
{
	sprintf(Tmp, "%I64d", X);
	int Len = strlen(Tmp);
	int Ptr = 0;
	for (int i = 0; i < Len; i ++)
		Tmp2[Ptr ++] = Tmp[i];
	for (int i = Len - 1; i >= 0; i --)
		Tmp2[Ptr ++] = Tmp[i];
	Tmp2[Ptr] = 0;
	long long Ret = 0;
	sscanf(Tmp2, "%I64d", &Ret);
	return Ret;
}

int Work(int Case)
{
	for (long long i = 1; i < 21474; i ++)
	{
		long long r = Kuo1(i);
		if (isP(r * r))
			printf("%I64d %I64d\n", r, r * r);
		r = Kuo2(i);
		if (isP(r * r))
			printf("%I64d %I64d\n", r, r * r);
	}
	return 1;
}

int main()
{
	Work(0);
	getchar();
	return 0;
}