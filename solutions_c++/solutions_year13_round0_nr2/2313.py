#include <iostream>
#include <string>
#include <stdlib.h>
#include <malloc.h>
#include <string.h>

int main(int argc, char *argv[])
{
	int nrTestCases;

	std::cin >> nrTestCases;

	for(int i = 0; i < nrTestCases; i++)
	{
		unsigned long N = 0, M = 0;

		std::cin >> N >> M;
		std::cout << "Case #" << (i+1) << ": ";

		// Invalid parameter?
		if (M < 1)
		{
			std::cout << "NO\n";
			continue;
		}

		// Allocate space
		unsigned char **alue = (unsigned char **)malloc(N*sizeof(long));
		unsigned char **pystyMerkit = (unsigned char **)malloc(N*sizeof(long));
		unsigned char **vaakaMerkit = (unsigned char **)malloc(N*sizeof(long));


		for(unsigned long j = 0; j < N; j++)
		{
			alue[j] = (unsigned char *)malloc(M*sizeof(unsigned char));
			pystyMerkit[j] = (unsigned char *)malloc(M*sizeof(unsigned char));
			vaakaMerkit[j] = (unsigned char *)malloc(M*sizeof(unsigned char));
			memset(alue[j], 0, M*sizeof(unsigned char));
			memset(pystyMerkit[j], 0, M*sizeof(unsigned char));
			memset(vaakaMerkit[j], 0, M*sizeof(unsigned char));
		}

		// Read the input
		for(int j = 0; j < N; j++)
		{
			for(int k = 0; k < M; k++)
			{
				std::cin >> alue[j][k];
			}
		}

		// Mark the situation
		// Ylh‰‰lt‰ alas
		for(int j = 0; j < M; j++)
		{
			// Etsi maksimiarvo
			int maxValue = 0;
			for(int k = 0; k < N; k++)
			{
				if (alue[k][j] > maxValue)
				{
					maxValue = alue[k][j];
				}
			}

			// T‰yt‰ rivi arvolla
			for(int k = 0; k < N; k++)
			{
				pystyMerkit[k][j] = maxValue;
			}
		}

		// Vasemmalta oikealle
		for(int k = 0; k < N; k++)
		{
			int maxValue = 0;
			for(int j = 0; j < M; j++)
			{
				if (alue[k][j] > maxValue)
				{
					maxValue = alue[k][j];
				}
			}

			// T‰yt‰ arvolla
			for(int j = 0; j < M; j++)
			{
				vaakaMerkit[k][j] = maxValue;
			}
		}

		// Test the squares
		for (int j = 0; j < N; j++)
		{
			for (int k = 0; k < M; k++)
			{
				if (alue[j][k] < vaakaMerkit[j][k] && alue[j][k] < pystyMerkit[j][k])
				{
					std::cout << "NO\n";
					goto cleanup;
				}
			}
		}

		std::cout << "YES\n";

		// Free space
		cleanup:
		for(unsigned long j = 0; j < N; j++)
		{
			free(alue[j]);
			free(pystyMerkit[j]);
			free(vaakaMerkit[j]);
		}
		free(alue);
		free(pystyMerkit);
		free(vaakaMerkit);
	}

	return 0;
}