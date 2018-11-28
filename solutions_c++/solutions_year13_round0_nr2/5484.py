#include <stdio.h>
#include <memory>
#include <cassert>

#define noPRINT_INPUT
#define noDEBUG

class Case
{
public:
	Case(int N, int M)
	{
		mN = N;
		mM = M;
		mYard = new int[mN*mM];
		mRow = new int[mN];
		mCol = new int[mM];

		for (int n=0; n<mN; ++n)
		{
			mRow[n] = 0;
		}
		for (int m=0; m<mM; ++m)
		{
			mCol[m] = 0;
		}
	}

	virtual ~Case()
	{
		delete [] mYard;
		delete [] mRow;
		delete [] mCol;
	}

	bool result()
	{
		bool result = true;

		// find max height
		int maxH = 0;
		for (int n=0; n<mN; ++n)
		{
			for (int m=0; m<mM; ++m)
			{
				int h = mYard[n*mM+m];
				if (h > maxH)
				{
					maxH = h;
				}

				if (mRow[n] == -1)
				{
					// failed row
				}
				else if (mRow[n] == 0)
				{
					mRow[n] = h;
				}
				else if (mRow[n] != h)
				{
					mRow[n] = -1;
				}

				if (mCol[m] == -1)
				{
				}
				else if (mCol[m] == 0)
				{
					mCol[m] = h;
				}
				else if (mCol[m] != h)
				{
					mCol[m] = -1;
				}
			}
		}

		for (int n=0; n<mN; ++n)
		{
			for (int m=0; m<mM; ++m)
			{
				if (mYard[n*mM+m] < maxH)
				{
					if ((mRow[n] == -1) && (mCol[m] == -1))
					{
						result = false;
						break;
					}
				}
			}
			if (result == false)
			{
				break;
			}
		}
		return result;
	}


	int* mYard;
private:
	int mN;
	int mM;
	int* mRow;
	int* mCol;
};

int main(int argc, char** argv)
{
	FILE* in = fopen(argv[1], "r");
	assert(in != NULL);

	int T = 0;
	fscanf(in, "%d\n", &T);
#ifdef PRINT_INPUT
	printf("T:%d\n", T);
#endif

	for (int t=0; t<T; ++t)
	{
		int N, M;
		fscanf(in, "%d %d\n", &N, &M);
#ifdef PRINT_INPUT
		printf("N:%d M:%d\n", N, M);
#endif
		Case c(N, M);
		for (int n=0; n<N; ++n)
		{
			for (int m=0; m<M; ++m)
			{
				fscanf(in, "%d ", &c.mYard[n*M+m]);
#ifdef PRINT_INPUT
				printf("%d ", c.mYard[n*M+m]);
#endif
			}
			fscanf(in, "\n");
#ifdef PRINT_INPUT
			printf("\n");
#endif
		}

		printf("Case #%d: %s\n", (t+1), c.result() ? "YES" : "NO");
	}

	fclose(in);
}