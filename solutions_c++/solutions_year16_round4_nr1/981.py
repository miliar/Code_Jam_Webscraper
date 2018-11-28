#include <ios>
#include <iostream>

int maximum(int a, int b, int c)
{
	if (a >= b && a >= c) return a;
	else if (b >= a && b >= c) return b;
	else return c;
}

int minimum(int a, int b, int c)
{
	if (a <= b && a <= c) return a;
	else if (b <= a && b <= c) return b;
	else return c;
}

void generate_answer(int p, int r, int s, int layer)
{
	//put as many p as you can on the left side
	//if you can put r, put that also
	//minimize s on left side BUT CONSTRAINTS HAVE TO BE FOLLOWED
	
	//max(r, s, p)-min(r, s, p) <= 1
	//for both sides
	
	if (layer > 1)
	{
		for (int i = p; i >= 0; i--)
		{
			for (int j = r; j >= 0; j--)
			{
				int k = (1 << (layer-1))-i-j;
				if (i >= 0 && j >= 0 && k >= 0 && p-i >= 0 && r-j >= 0 && s-k >= 0)
				{
					if (maximum(i, j, k) - minimum(i, j, k) <= 1 && maximum(p-i, r-j, s-k) - minimum(p-i, r-j, s-k) <= 1)
					{
 						generate_answer(i, j, k, layer-1);
						generate_answer(p-i, r-j, s-k, layer-1);
						return;
					}
				}
			}
		}
	}
	else
	{
		if (p == 1 && r == 1) std::cout << "PR";
		else if (p == 1 && s == 1) std::cout << "PS";
		else if (r == 1 && s == 1) std::cout << "RS";
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc, n, p, r, s;
	std::cin >> tc;
	for (int t = 0; t < tc; t++)
	{
		std::cout << "Case #" << t+1 << ": ";
		std::cin >> n >> r >> p >> s;
		if (maximum(p, r, s) - minimum(p, r, s) <= 1)
		{
			generate_answer(p, r, s, n);
			std::cout << '\n';
		}
		else
		{
			std::cout << "IMPOSSIBLE" << '\n';
		}
	}
}
