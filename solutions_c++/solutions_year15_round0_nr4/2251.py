#include <iostream>

#define min(a, b) ((a) < (b) ? (a) : (b))
#define max(a, b) ((a) > (b) ? (a) : (b))

enum Winner
{
	R, G
};

Winner win_table[4][4][4] = 
{
	/* 1-omino */
	{
		/* 1-by- */
		{
			/* 1, 2, 3 4 */
			G, G, G, G
		},
		/* 2-by- */
		{
			G, G, G, G
		},
		/* 3-by- */
		{
			G, G, G, G
		},
		/* 4-by- */
		{
			G, G, G, G
		}
	},

	/* 2-omino */
	{
		/* 1-by- */
		{
			/* 1, 2, 3 4 */
			R, G, R, G
		},
		/* 2-by- */
		{
			G, G, G, G
		},
		/* 3-by- */
		{
			R, G, R, G
		},
		/* 4-by- */
		{
			G, G, G, G
		}
	},

	/* 3-omino */
	{
		/* 1-by- */
		{
			/* 1, 2, 3 4 */
			R, R, R, R
		},
		/* 2-by- */
		{
			R, R, G, R
		},
		/* 3-by- */
		{
			R, G, G, G
		},
		/* 4-by- */
		{
			R, R, G, R
		}
	},

	/* 4-omino */
	{
		/* 1-by- */
		{
			/* 1, 2, 3 4 */
			R, R, R, R
		},
		/* 2-by- */
		{
			R, R, R, R
		},
		/* 3-by- */
		{
			R, R, R, G
		},
		/* 4-by- */
		{
			R, R, G, G
		}
	},
};



int main()
{
	int T;
	std::cin >> T;
	for (int c = 1; c <= T; ++c) {
		int X, R, C;
		std::cin >> X >> R >> C;
		std::cout << "Case #" << c << ": " << (win_table[X-1][R-1][C-1] == Winner::R ? "RICHARD" : "GABRIEL") << '\n';
	}
	
	return 0;
}