#include "stdafx.h"


void SolveA(Int N)
{
	for (int n = 0; n < N; n++)
	{
		Int Smax = ReadNum();
		Int need = 0;
		Int sum = 0;
		for (Int i = 0; i < Smax + 1; i++)
		{
			if (sum > Smax)
			{
				ReadStr();
				break;
			}
			char c = ReadChar();
			Int d = c - '0';
			sum += d;
			if (i + 1 - sum > 0) {
				need += i + 1 - sum;
				sum = i + 1;
			}
		}
		Write(n + 1, need);
	}
}