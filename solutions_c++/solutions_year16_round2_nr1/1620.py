#pragma once


template<>
struct CTXData<ProblemA>
{
	Str all;

	map<char, Int> count;
	Int Count(char * num, char c)
	{
		Int r = count[c];
		while (num[0])
		{
			count[num[0]] -= r;
			num++;
		}
		return r;
	}
};

template<>
void CTX<ProblemA>::Read()
{
	all = ReadStr();
}


template<>
void CTX<ProblemA>::Solve()
{
	for (Int i = 0; i < all.size(); i++)
	{
		count[all[i]]++;
	}
	Int nums[10];
	nums[2] = Count("TWO", 'W');
	nums[8] = Count("EIGHT", 'G');
	nums[3] = Count("THREE", 'T');
	nums[6] = Count("SIX", 'X');
	nums[7] = Count("SEVEN", 'S');
	nums[5] = Count("FIVE", 'V');
	nums[4] = Count("FOUR", 'F');
	nums[9] = Count("NINE", 'I');
	nums[1] = Count("ONE", 'N');
	nums[0] = Count("ZERO", 'Z');
	Str res;
	for (Int i = 0; i < 10; i++)
	{
		if (nums[i])
		{
			res.append(nums[i], '0' + i);
		}
	}
	Write(res);
}