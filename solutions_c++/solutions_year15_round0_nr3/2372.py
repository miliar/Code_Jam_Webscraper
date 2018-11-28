#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

#define MULTITHREADED

#ifdef MULTITHREADED
#include <thread>
#endif

using namespace std;

#define uint	unsigned int

enum E_QUAT_ID
{
	EQI_1,
	EQI_i,
	EQI_j,
	EQI_k,
	EQI_m1,
	EQI_mi,
	EQI_mj,
	EQI_mk,

	EQI_COUNT
};
const E_QUAT_ID multTable[EQI_COUNT][EQI_COUNT] = {
	{ EQI_1, EQI_i, EQI_j, EQI_k, EQI_m1, EQI_mi, EQI_mj, EQI_mk },
	{ EQI_i, EQI_m1, EQI_k, EQI_mj, EQI_mi, EQI_1, EQI_mk, EQI_j },
	{ EQI_j, EQI_mk, EQI_m1, EQI_i, EQI_mj, EQI_k, EQI_1, EQI_mi },
	{ EQI_k, EQI_j, EQI_mi, EQI_m1, EQI_mk, EQI_mj, EQI_i, EQI_1 },
	{ EQI_m1, EQI_mi, EQI_mj, EQI_mk, EQI_1, EQI_i, EQI_j, EQI_k },
	{ EQI_mi, EQI_1, EQI_mk, EQI_j, EQI_i, EQI_m1, EQI_k, EQI_mj },
	{ EQI_mj, EQI_k, EQI_1, EQI_mi, EQI_j, EQI_mk, EQI_m1, EQI_i },
	{ EQI_mk, EQI_mj, EQI_i, EQI_1, EQI_k, EQI_j, EQI_mi, EQI_m1 } };
E_QUAT_ID operator*(E_QUAT_ID x, E_QUAT_ID y)
{
	/*
	switch (x)
	{
	case EQI_i:
		switch (y)
		{
		case EQI_1:		return EQI_i;
		case EQI_i:		return EQI_m1;
		case EQI_j:		return EQI_k;
		case EQI_k:		return EQI_mj;
		case EQI_m1:	return EQI_mi;
		case EQI_mi:	return EQI_1;
		case EQI_mj:	return EQI_mk;
		case EQI_mk:	return EQI_j;
		}
	case EQI_j:
		switch (y)
		{
		case EQI_1:		return EQI_j;
		case EQI_i:		return EQI_mk;
		case EQI_j:		return EQI_m1;
		case EQI_k:		return EQI_i;
		case EQI_m1:	return EQI_mj;
		case EQI_mi:	return EQI_k;
		case EQI_mj:	return EQI_1;
		case EQI_mk:	return EQI_mi;
		}
	case EQI_k:
		switch (y)
		{
		case EQI_1:		return EQI_k;
		case EQI_i:		return EQI_j;
		case EQI_j:		return EQI_mi;
		case EQI_k:		return EQI_m1;
		case EQI_m1:	return EQI_mk;
		case EQI_mi:	return EQI_mj;
		case EQI_mj:	return EQI_i;
		case EQI_mk:	return EQI_1;
		}
	case EQI_m1:
		switch (y)
		{
		case EQI_1:		return EQI_m1;
		case EQI_i:		return EQI_mi;
		case EQI_j:		return EQI_mj;
		case EQI_k:		return EQI_mk;
		case EQI_m1:	return EQI_1;
		case EQI_mi:	return EQI_i;
		case EQI_mj:	return EQI_j;
		case EQI_mk:	return EQI_k;
		}
	case EQI_mi:
		switch (y)
		{
		case EQI_1:		return EQI_mi;
		case EQI_i:		return EQI_1;
		case EQI_j:		return EQI_mk;
		case EQI_k:		return EQI_j;
		case EQI_m1:	return EQI_i;
		case EQI_mi:	return EQI_m1;
		case EQI_mj:	return EQI_k;
		case EQI_mk:	return EQI_mj;
		}
	case EQI_mj:
		switch (y)
		{
		case EQI_1:		return EQI_mj;
		case EQI_i:		return EQI_k;
		case EQI_j:		return EQI_1;
		case EQI_k:		return EQI_mi;
		case EQI_m1:	return EQI_j;
		case EQI_mi:	return EQI_mk;
		case EQI_mj:	return EQI_m1;
		case EQI_mk:	return EQI_i;
		}
	case EQI_mk:
		switch (y)
		{
		case EQI_1:		return EQI_mk;
		case EQI_i:		return EQI_mj;
		case EQI_j:		return EQI_i;
		case EQI_k:		return EQI_1;
		case EQI_m1:	return EQI_k;
		case EQI_mi:	return EQI_j;
		case EQI_mj:	return EQI_mi;
		case EQI_mk:	return EQI_m1;
		}
	default:			return y;
	}
	*/
	return multTable[x][y];
}
E_QUAT_ID operator*=(E_QUAT_ID& x, E_QUAT_ID y)
{
	x = x * y;
	return x;
}
E_QUAT_ID charToQuadId(char c)
{
	switch (c)
	{
	case 'i':	return EQI_i;
	case 'j':	return EQI_j;
	case 'k':	return EQI_k;
	default:	return EQI_1;
	}
}
bool canReduce(string str, int X)
{
	// Optimisation : pour tout E_QUAT_ID z : z^4 = 1
	//X = X % 4;

	const int strRealSize = (int)str.size();
	const int strTotalSize = strRealSize * X;
	E_QUAT_ID valI = EQI_1;
	for (int x = 0; x < strTotalSize; x++)
	{
		valI *= charToQuadId(str[x % strRealSize]);
		if (valI == EQI_i)
		{
			E_QUAT_ID valJ = EQI_1;
			for (int y = x + 1; y < strTotalSize; y++)
			{
				valJ *= charToQuadId(str[y % strRealSize]);
				if (valJ == EQI_j)
				{
					E_QUAT_ID valK = EQI_1;
					for (int z = y + 1; z < strTotalSize; z++)
					{
						valK *= charToQuadId(str[z % strRealSize]);
						if (valK == EQI_k && z == strTotalSize - 1)
							return true;
					}
				}
			}
		}
	}
	return false;
}

#ifdef MULTITHREADED
struct Input
{
	int X;
	string str;

	Input() : X(-1) { }
};
Input inputs[100];
bool results[100];
void threadCompute(int start, int end)
{
	for (int i = start; i < end; i++)
		if (inputs[i].X > 0)
			results[i] = canReduce(inputs[i].str, inputs[i].X);
}
#endif
int main()
{
	int nbTests;
	cin >> nbTests;
#ifndef MULTITHREADED
	for (int testId = 0; testId < nbTests; testId++)
	{
		int L, X;
		string str;
		cin >> L >> X >> str;
		cout << "Case #" << testId + 1 << ": " << (const char*)(canReduce(str, X) ? "YES" : "NO") << endl;
	}
#else
	for (int testId = 0; testId < nbTests; testId++)
	{
		int L;
		cin >> L >> inputs[testId].X >> inputs[testId].str;
	}

#define NB_THREADS	8
	thread* threads[NB_THREADS];
	const int resultsPerThread = nbTests / NB_THREADS;
	for (int i = 0; i < NB_THREADS - 1; i++)
		threads[i] = new thread(threadCompute, i * resultsPerThread, (i + 1) * resultsPerThread);
	threads[NB_THREADS - 1] = new thread(threadCompute, (NB_THREADS - 1) * resultsPerThread, nbTests);
	for (int i = 0; i < NB_THREADS; i++)
	{
		threads[i]->join();
		delete (threads[i]);
	}

	for (int testId = 0; testId < nbTests; testId++)
		cout << "Case #" << testId + 1 << ": " << (const char*)(results[testId] ? "YES" : "NO") << endl;
#endif

#ifdef _DEBUG
	_CrtDbgBreak();
#endif
	return EXIT_SUCCESS;
}
