#include <iostream>
#include <iomanip>

using namespace std;

void main()
{
	unsigned long long t, ti, n, j, c, b, esPrimo, cjj, cesPrimo;
	unsigned long long nb, cj, m, s;
	unsigned long long nn[9];
	unsigned long long nnn[9];
	unsigned long long p[10][32];

	int primos[] = {2,3,5,7,11,13,17,19,23,29,31,37,41,42,43,47,53,59,61,67,71,73,
		79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,
		191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,
		311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,
		439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,
		577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,
		709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,
		857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997 };

	for (int bi = 2; bi <= 10; bi++)
		for (int pi = 0; pi <= 32; pi++)
			p[bi - 2][pi] = pow(bi, pi);

	cin >> t;
	for (ti = 1; ti <= t; ti++)
	{
		cin >> n >> j;
		cout << "Case #" << ti << ":" << endl;
		for (c = 0, cjj = 0; c < p[0][n - 2]; c++)
		{
			cj = (1 << (n - 1)) | (c << 1) | 1;

			for (b = 2, cesPrimo = 0; b <= 10; b++)
			{
				for (nb = 0, s = 0; s < n; s++)
					nb += (cj & (1 << s)) ? p[b - 2][s] : 0;
				nn[b - 2] = nb;
				for (s = 0, esPrimo = 1; s < 168; s++)
					if (nb % primos[s] == 0)
					{
						esPrimo = 0;
						nnn[b - 2] = primos[s];
						break;
					}

				if (!esPrimo) cesPrimo++;
				else break;
			}

			if (cesPrimo == 9)
			{
				cout << nb << " ";
				for (s = 0; s < 9; s++)
					cout << nnn[s] << " ";
				cout << endl;
				cjj++;
			}

			if (cjj == j) break;
		}
	}
}