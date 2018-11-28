#include "stdafx.h"

Int gcd ( Int a, Int b )
{
  int c;
  while ( a != 0 ) {
     c = a; a = b%a;  b = c;
  }
  return b;
}

Int LowestBit(Int i)
{
	if (i & 1)
		return 0;
	else
		return 1+LowestBit(i/2);
}
Int HBit(Int i)
{
	if (i)
		return 1+HBit(i/2);
	else
		return 0;
}

void SovleA(char * input)
{
	TRACE("started...");
	Int T; READ(T); NL;
	for (Int t = 0; t < T; t++)
	{
		char skipped;
		Int P; Int Q; READ(P); READ(skipped); READ(Q); NL;
		Int m = gcd(P, Q);
		P /= m;
		Q /= m;
		Int p = HBit(P) - 1;
		Int q = LowestBit(Q);
		Int l = LowestBit(P);
		if (q <= p)
			PRINT("Case #%I64d: impossible\n", t + 1);
		else
			PRINT("Case #%I64d: %I64d\n", t + 1, q - p);
	}
	TRACE("ended.");
}