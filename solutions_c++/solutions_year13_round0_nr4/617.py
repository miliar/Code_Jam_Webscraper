/*******************************************************************************
*	GoogleCodeJamQualificationD
*	Christoper Mayer, aka Quantum Anemone
*******************************************************************************/

/*
Problem


*/

#include	<Windows.h>
#include	<stdio.h>
#include	<conio.h>
#include	<map>

FILE	*inputFile;
FILE	*outputFile;

#define	MAX_KEYS	400
#define	MAX_CHESTS	200
int		nKeys, nChests, keysIHave[MAX_KEYS], opener[MAX_CHESTS], has[MAX_CHESTS], hasKey[MAX_CHESTS][MAX_KEYS], sequence[MAX_CHESTS];
bool	opened[MAX_CHESTS];

// lets add a list of previous failures
struct SEQUENCE_TEST
{
	unsigned __int64	a[4];	// 256 max chests, 1 bit each
	bool operator<(const SEQUENCE_TEST &b) const
	{
		for (int i=0; i<4; i++)
			if (a[i] != b.a[i]) return a[i] < b.a[i];
		return false;
	}
};
SEQUENCE_TEST	foo = {0,0,0,0};
std::map<SEQUENCE_TEST,char>	failed;

void bitSet(unsigned char *d, int b)
{
	d[b/8] |= 1 << (b%8);
}

void bitReset(unsigned char *d, int b)
{
	d[b/8] &= 0xFF ^ (1 << (b%8));
}


bool solveR(int	nChestsLeft)
{
	if (nChestsLeft == 0)
		return true;
	if (nKeys == 0)
		return false;
	for (int c=0; c<nChests; c++)
	{
		if (opened[c])
			continue;
		// do I have the right key?
		if (keysIHave[opener[c]] == 0)
			continue;
		{
			{
				// remember the sequence
				sequence[nChestsLeft] = c;

				// use the key to...
				keysIHave[opener[c]]--;
				nKeys--;
				// open the chest
				opened[c] = true;
				bitSet((unsigned char *)&foo, c);
				// get new keys from inside
				for (int k=0; k<has[c]; k++)
					keysIHave[hasKey[c][k]]++;
				nKeys += has[c];

				// recursivly look for the solution
				if (failed.find(foo) == failed.end())	// already failed this permutated sub sequence?
				{
					if (solveR(nChestsLeft-1))
					{
						// put back the keys in the chest
						for (int k=0; k<has[c]; k++)
							keysIHave[hasKey[c][k]]--;
						nKeys -= has[c];
						// close the chest
						opened[c] = false;
						bitReset((unsigned char *)&foo, c);
						// get back the key used to open it
						keysIHave[opener[c]]++;
						nKeys++;
						return true;
					}
					else
					{
						// remember our failure for pruning
						failed[foo] = ' ';
					}
				}

				// put back the keys in the chest
				for (int k=0; k<has[c]; k++)
					keysIHave[hasKey[c][k]]--;
				nKeys -= has[c];
				// close the chest
				opened[c] = false;
				bitReset((unsigned char *)&foo, c);
				// get back the key used to open it
				keysIHave[opener[c]]++;
				nKeys++;
			}
		}
	}
	return false;
}

void solve(void)
{
	// reset the failed map
	failed.clear();

	fscanf_s(inputFile, "%d", &nKeys);
	fscanf_s(inputFile, "%d", &nChests);
	//printf("%d keys, %d chests.\n", nKeys, nChests);
	for (int i=0; i<MAX_KEYS; i++)
		keysIHave[i] = 0;
	for (int i=0; i<nKeys; i++)
	{
		int k;
		fscanf_s(inputFile, "%d", &k);
		keysIHave[k]++;
	}
	for (int i=0; i<nChests; i++)
	{
		opened[i] = false;
		fscanf_s(inputFile, "%d", &opener[i]);
		fscanf_s(inputFile, "%d", &has[i]);
		for (int j=0; j<has[i]; j++)
		{
			fscanf_s(inputFile, "%d", &hasKey[i][j]);
		}
	}

	if (solveR(nChests))
	{
		for (int i=nChests; i>0; i--)
		{
			printf_s("%d ", sequence[i]+1);
			fprintf_s(outputFile, "%d ", sequence[i]+1);
		}
		printf_s("\n");
		fprintf_s(outputFile, "\n");
	}
	else
	{
		printf_s("IMPOSSIBLE\n");
		fprintf_s(outputFile, "IMPOSSIBLE\n");
	}
}

void main(int argc, char *argv[])
{
	unsigned __int64	frequency, t0, t1;

	QueryPerformanceCounter((LARGE_INTEGER *)&t0);

	printf_s("GoogleCodeJamQualificationB\n");
	printf_s("Christoper Mayer, aka Quantum Anemone\n\n");

	// create output file
	char	outputFilename[256];
	sprintf_s(outputFilename, "%s.out", argv[1]);
	fopen_s(&outputFile, outputFilename, "w");
	printf_s("This program may output debug info to the console.\n");
	printf_s("The official output is written to the file %s.\n\n", outputFilename);

	// open input file
	fopen_s(&inputFile, argv[1], "r");

	// how many cases?
	int	nCases;
	fscanf_s(inputFile, "%d", &nCases);

	// solve them!
	for (int i=1; i<=nCases; i++)
	{
		printf_s("Case #%d: ", i);
		fprintf_s(outputFile, "Case #%d: ", i);
		solve();
	}

	// clean up
	fclose(inputFile);
	fclose(outputFile);

	QueryPerformanceCounter((LARGE_INTEGER *)&t1);
	QueryPerformanceFrequency((LARGE_INTEGER *)&frequency);
	printf_s("\nAll finished in %f seconds.\n", (t1-t0)/(float)frequency);
	_getch();
}
