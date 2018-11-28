#include "stdafx.h"
#include <algorithm>

void SolveD(Int N)
{
	//N = 64;
	for (Int n = 0; n < N; n++)
	{
		Int X, R, C;
		//X = n % 4 + 1;// ReadNum();
		//R = (n / 4) % 4 + 1;// ReadNum();
		//C = (n / 16) % 4 + 1; // ReadNum();
		X = ReadNum();
		R = ReadNum();
		C = ReadNum();
		if ((X + 1) / 2 > min(R, C)) {
			Write(n + 1, "RICHARD");
			continue;
		}
		if ((R * C) % X != 0) {
			Write(n + 1, "RICHARD");
			continue;
		}
		if (min(R, C) < (X+1) / 2) {
			Write(n + 1, "RICHARD");
			continue;
		}
		if (max(R, C) < X) {
			Write(n + 1, "RICHARD");
			continue;
		}
		if (max(R, C) > X) {
			Write(n + 1, "GABRIEL");
			continue;
		}
		if (X < 4) {
			Write(n + 1, "GABRIEL");
			continue;
		}
		if (X > 6) {
			Write(n + 1, "RICHARD");
			continue;
		}
		if (min(R, C) < 3) {
			Write(n + 1, "RICHARD");
			continue;
		}
		Write(n + 1, "GABRIEL");
		continue;
	}
}