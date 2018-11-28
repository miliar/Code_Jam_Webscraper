#include "stdafx.h"

#include <set>
#include <map>

map<Int, map<Int, Int> > turns;
void InitTurns(Int upTo)
{
	turns[1][1] = 0;
	for (Int i = 2; i <= upTo; i++)
	{
		for (Int asLow = 1; asLow < i; asLow++)
		{
			Int lowest = i;
			for (Int step = asLow; step < i; step++)
			{
				Int newLow = turns[step][asLow] + turns[i - step][asLow] + 1;
				if (newLow < lowest)
					lowest = newLow;
			}
			turns[i][asLow] = lowest;
		}
	}
}
void SolveB(Int N)
{
	InitTurns(9);
	for (Int n = 0; n < N; n++)
	{
		Int D = ReadNum();
		Int r = 0;
		multiset<Int> Dset;
		for (Int d = 0; d < D; d++)
		{
			Dset.insert(ReadNum());
		}
		Int best = *Dset.rbegin();
		Int curr = best;
		while (curr > 1)
		{
			curr--;
			Int cost = 0;
			for (multiset<Int>::reverse_iterator it = Dset.rbegin(); it != Dset.rend(); ++it)
			{
				if (*it <= curr) {
					//cost = best;
					break;
				}
				cost += turns[*it][curr];
				if (cost + curr >= best) {
					break;
				}
			}
			if (cost + curr < best)
			{
				best = cost + curr;
			}
		}
		Write(n + 1, best);
	}
}