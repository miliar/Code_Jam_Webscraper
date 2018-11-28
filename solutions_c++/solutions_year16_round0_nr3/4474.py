#pragma once


template<>
struct CTXData<ProblemC>
{
	Int N, J;
	Int inBases[11];
	void InitBases()
	{
		for (Int i = 2; i < 11; i++) {
			inBases[i] = 1 + pow(i, N - 1);
		}
	}
	Int Delimiter(Int n)
	{
		if ((n & 1) == 0) return 2;
		Int limit = (Int)sqrt(n);
		for (Int i = 3; i <= limit; i+=2)
		{
			if (n % i == 0)
				return i;
		}
		return 1;
	}
	Str Base2()
	{
		Int n = inBases[2];
		char buffer[64];
		itoa(n, buffer, 2);
		return buffer;
	}
	bool NoPrimes(Int * outDelimiters)
	{
		for (Int i = 2; i < 11; i++)
		{
			Int d = Delimiter(inBases[i]);
			if (d != 1)
			{
				outDelimiters[i] = d;
			}
			else
			{
				return false;
			}
		}
		return true;
	}
	void NextBases()
	{
		Int prevBase2 = inBases[2];
		inBases[2] += 2;
		for (Int i = 1; i < N - 1; i++)
		{
			Int prevBit = (prevBase2 >> i) & 1;
			Int newBit = (inBases[2] >> i) & 1;
			if (prevBit != newBit)
			{
				if (prevBit == 0)
				{
					for (Int b = 3; b < 11; b++)
					{
						inBases[b] += pow(b, i);
					}
				}
				else
				{
					for (Int b = 3; b < 11; b++)
					{
						inBases[b] -= pow(b, i);
					}
				}
			}
		}
	}
};

template<>
void CTX<ProblemC>::Read()
{
	N = ReadNum();
	J = ReadNum();
}

template<>
void CTX<ProblemC>::Solve()
{
	Str result = "";
	InitBases();
	Int i = 0;
	while (i < J)
	{
		Int ds[11];
		if (NoPrimes(ds))
		{
			result += "\n";

			result += Base2();

			for (Int j = 2; j < 11; j++)
			{
				result += " ";

				char buffer[64];
				itoa(ds[j], buffer, 10);
				result += buffer;
			}
			i++;
		}
		NextBases();
	}
	Write(result);
}