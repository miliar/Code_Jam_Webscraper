#include <cstdlib>
#include <cstdio>
#include <fstream>
#include <stdint.h>
#include <vector>
#include <algorithm>

using namespace std;

vector<uint64_t> base;


bool is_palindrome(uint64_t x)
{
	uint64_t y = x, rev_x = 0;

	while (y)
	{
		rev_x = rev_x*10 + y%10;
		y /=  10;
	}

	return (x == rev_x);
}


void precompute_base()
{
	int 		a, b;
	uint64_t	x, y;

	// 1-digit roots
	for (int i = 0; i <= 3; i++)
	{
		base.push_back(i);
	}

	a = 1;
	b = 10;

	for (int k = 0; k < 4; k++)
	{
		// add even palindrome
		for (int i = a; i < b; i++)
		{
			x = i;
			y = i;

			while (y)
			{
				x = 10*x + y%10;
				y /= 10;
			}

			if (is_palindrome(x*x)) base.push_back(x);
		}

		// add odd palindromes
		for (int i = a; i < b; i++)
		{
			for (int mid = 0; mid <= 9; mid++)
			{
				x = i * 10 + mid;
				y = i;

				while (y)
				{
					x = 10*x + y%10;
					y /= 10;
				}

				if (is_palindrome(x*x)) base.push_back(x);
			}
		}

		a *= 10;
		b *= 10;
	}
}


int binary_search(uint64_t x)
{
	int 		a, b, mid, res;
	uint64_t	sq;

	a = 0;
	b = base.size() - 1;
	while (a <= b)
	{
		mid = (a + b) / 2;
		sq	= base[mid] * base[mid];

		if (sq == x) return mid;

		if (sq > x)
		{
			b = mid - 1;
		}
		else
		{
			a 	= mid + 1;
			res = mid;
		}
	}

	return res;
}


int solve(uint64_t A, uint64_t B)
{
	return binary_search(B) - binary_search(A - 1);
}


int main()
{
	fstream		f, g;
	int			tests;
	uint64_t	a, b;

	f.open("in.txt", ios :: in);
	g.open("out.txt", ios :: out);

	precompute_base();

	f >> tests;
	for (int k = 1; k <= tests; k++)
	{
		f >> a >> b;
		g << "Case #" << k << ": " << solve(a, b) << endl;
	}

	f.close();
	g.close();

	return 0;
}
