#pragma once


template<>
struct CTXData<ProblemA>
{
	Int N;
	std::set<Int> digits;
	bool ExtractDigits(Int n)
	{
		while (n)
		{
			digits.insert(n % 10);
			n /= 10;
		}
		return digits.size() == 10;
	}
};

template<>
void CTX<ProblemA>::Read()
{
	N = ReadNum();
}

template<>
void CTX<ProblemA>::Solve()
{
	if (N == 0) {
		Write("INSOMNIA");
		return;
	}
	Int C = N;
	while (!ExtractDigits(C))
	{
		C += N;
	}
	Write(C);
}