#pragma once

template<>
struct CTXData<ProblemB>
{
	Str all;
};

template<>
void CTX<ProblemB>::Read()
{
	all = ReadStr();
}

template<>
void CTX<ProblemB>::Solve()
{
	Int res = 1;
	char c = all[0];
	for (Int i = 1; i < all.size(); i++)
	{
		if (c != all[i])
		{
			c = all[i];
			res++;
		}
	}
	if (c == '+') res--;
	Write(res);
}