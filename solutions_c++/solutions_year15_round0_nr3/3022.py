// problem_c.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <vector>
#include <assert.h>

struct sIJK
{
	enum Q
	{
		e1 = 1,
		eI,
		eJ,
		eK
	};

	sIJK() : v(e1) {}

	sIJK(char c)
	{
		switch (c)
		{
		case 'i':
			v = eI;
			break;
		case 'j':
			v = eJ;
			break;
		case 'k':
			v = eK;
			break;
		default:
			break;
		}
	}
	int v;

	static const int M[4][4];

	sIJK& operator *= (const sIJK& rhs)
	{
		v = ((v * rhs.v) > 0 ? 1 : -1) * M[abs(v)-1][abs(rhs.v)-1];
		return *this;
	}
};

sIJK operator * (const sIJK& lhs, const sIJK& rhs)
{
	sIJK v;
	v.v = ((lhs.v * rhs.v) > 0 ? 1 : -1) * sIJK::M[abs(lhs.v)-1][abs(rhs.v)-1];
	return v;
}

const int sIJK::M[4][4] = { { e1, eI, eJ, eK }, { eI, -e1, eK, -eJ }, { eJ, -eK, -e1, eI }, { eK, eJ, -eI, -e1 } };

void getI(const std::vector<sIJK>& v, std::vector<int>& res)
{
	sIJK acc;
	for (int i = 0; i != v.size(); ++i)
	{
		acc = acc * v[i];
		if (acc.v == sIJK::eI)
			res.push_back(i+1);
	}
}

sIJK isJ(const std::vector<sIJK>& v, int start, int end)
{
	assert(start < end);
	sIJK res;
	for (int i = start; i < end; ++i)
	{
		res *= v[i];
	}
	return res;
}

void getK(const std::vector<sIJK>& v, std::vector<int>& res)
{
	sIJK acc;
	for (int i = v.size() - 1; i >= 0; --i)
	{
		acc = v[i] * acc;
		if (acc.v == sIJK::eK)
			res.push_back(i);
	}
}

const char* Case(std::ifstream& in)
{
	std::vector<sIJK> input;

	int L = 0;
	in >> L;

	int X = 0;
	in >> X;

	std::vector<sIJK> w;
	for (int i = 0; i < L; i++)
	{
		unsigned char c = 0;
		in >> c;
		w.push_back(sIJK(c));
	}

	for (int i = 0; i < X; ++i)
		input.insert(input.end(), w.begin(), w.end());

	std::vector<int> Ires;
	getI(input, Ires);

	std::vector<int> Kres;
	getK(input, Kres);
	std::reverse(Kres.begin(), Kres.end());
	
	for (int i : Ires)
	{
		sIJK last;
		int curr = i;
		for (int k : Kres)
		{
			if (i >= k)
				continue;

			last *= isJ(input, curr, k);
			curr = k;
			if (last.v == sIJK::eJ)
				return "YES";
		}
	}

	return "NO";
}

void Run(const char* in, const char* out)
{
	std::ifstream input;
	input.open(in);

	int cases = 0;
	input >> cases;

	std::vector<const char*> res;
	for (int i = 0; i < cases; ++i)
	{
		res.push_back(Case(input));
		std::cout << i << "\n";
	}

	input.close();

	std::ofstream output;
	output.open(out);
	for (int i = 0; i < cases; ++i)
		output << "Case #" << i+1 << ": " << res[i] << "\n";
	output.close();
}

int _tmain(int argc, _TCHAR* argv[])
{
	Run("C-small-attempt2.in", "output_c");
	return 0;
}
