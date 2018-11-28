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

//--------------------------------------------------------------------------------------------------
void ProcessTask(int in_id)
{
	int n, m;
	cin >> n;
	cin >> m;
	int map[100][100];

	for(int i = 0; i < n; ++i)
	{
		for(int j = 0; j < m; ++j)
		{
			cin >> map[i][j];
		}
	}

	int max_n[100];
	for(int i = 0; i < n; ++i)
	{
		int k = map[i][0];
		for(int j = 1; j < m; ++j)
			if (map[i][j] > k) k = map[i][j];
		max_n[i] = k;
	}

	int max_m[100];
	for(int j = 0; j < m; ++j)
	{
		int k = map[0][j];
		for(int i = 1; i < n; ++i)
			if (map[i][j] > k) k = map[i][j];
		max_m[j] = k;
	}

	bool res = true;
	for(int i = 0; (i < n) && res; ++i)
	{
		for(int j = 0; j < m; ++j)
			if ((map[i][j] != max_n[i]) && (map[i][j] != max_m[j]))
			{
				res = false;
				break;
			}
	}

	printf("Case #%d: %s\n", in_id + 1, res ? "YES" : "NO");
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
