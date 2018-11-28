#define _SECURE_SCL 0

#include <iostream>
#include <math.h>
#include <vector>
#include <algorithm>

using namespace std;

#ifdef _DEBUG
#define	Assert(E)		do { if (!(E)) {  __asm {int 3}; } } while (false)
#else// _DEBUG
#define	Assert(E)		do { if (!(E)) {  __asm {int 3}; } } while (false)
//#define	Assert(E)		do { if (!(E)) { } } while (false)
#endif//_DEBUG

typedef unsigned long DWORD;
typedef unsigned char BYTE;
typedef unsigned __int64 QWORD;

char str[1000];

//--------------------------------------------------------------------------------------------------
bool IsPalindrom(int a)
{
	if (a == 0) return false;

	int i = -1;
	while(a)
	{
		str[++i] = a % 10;
		a = a / 10;
	}

	for(int j = 0; j <= i; ++j, --i)
		if (str[j] != str[i])
			return false;
	return true;
}

//--------------------------------------------------------------------------------------------------
void ProcessTask(int in_id)
{
	int a, b;
	cin >> a;
	cin >> b;

	int counter = 0;
	int a1 = int(sqrt(double(a))) - 1;
	int b1 = int(sqrt(double(b))) + 1;
	for(int i = a1; i <= b1; ++i)
	{
		int s = i * i;
		if (s < a) continue;
		if (s > b) break;
		if (IsPalindrom(i) && IsPalindrom(s))
			++counter;
	}

	printf("Case #%d: %d\n", in_id + 1, counter);
}

//--------------------------------------------------------------------------------------------------
int main()
{
	int numb;
	cin >> numb;

	for(int i = 0; i < numb; ++i)
	{
		ProcessTask(i);
	}

	return 0;
}
