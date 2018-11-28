#include <cstdio>
#include <cassert>
#include <fstream>
#include <cmath>

#define noVERBOSE_INPUT
#define noDEBUG

#define MAX_LINE	256
#define MAX_NUM		101

class StrNum
{
public:
	StrNum(int n)
	{
		memset(mN, 0, MAX_NUM);

		int i = 0;
		while (n > 0)
		{
			mN[i++] = n % 10;
			n /= 10;
		}
		mLen = i;
	}

	bool checkFair()
	{
		bool fair = true;

		int l = 0;
		int r = mLen - 1;

		while (l <= r)
		{
			if (mN[l] != mN[r])
			{
				fair = false;
				break;
			}

			++l;
			--r;
		}

		return fair;
	}

private:
	char mN[MAX_NUM];
	int mLen;
};

class Numbers
{
public:
	Numbers(int A, int B)
	{
		mA = A;
		mB = B;
		mSqrtA = (int)(sqrt((double)A));
		mSqrtB = (int)(sqrt((double)B)) + 1;
#ifdef DEBUG
		printf("mSqrt:%d %d\n", mSqrtA, mSqrtB);
#endif
	}
	virtual ~Numbers() 
	{
	}

	int result()
	{
		int result = 0;

		for (int i=mSqrtA; i<=mSqrtB; ++i)
		{
			if (checkFairAndSquare(i))
			{
				++result;
			}
		}

		return result;
	}

private:
	bool checkFairAndSquare(int n)
	{
		bool result = false;
		StrNum sn(n);
		if (sn.checkFair())
		{
#ifdef DEBUG
			printf("%d is fair.\n", n);
#endif
			int n2 = n*n;
			if ((n2 >= mA) && (n2 <= mB))
			{
				StrNum sn2(n2);
				if (sn2.checkFair())
				{
#ifdef DEBUG
					printf("^2 %d is fair.\n", n2);
#endif
					result = true;
				}
			}
		}
		return result;
	}

	int mA;
	int mB;
	int mSqrtA;
	int mSqrtB;
};

int main(int argc, char** argv)
{
	std::ifstream in(argv[1]);
	int T = 0;

	char line[MAX_LINE];
	memset(line, 0, MAX_LINE);
	in.getline(line, MAX_LINE);
	T = atoi(line);
	
	for (int t=0; t<T; ++t)
	{
		int A, B;
		in.getline(line, MAX_LINE);
		char* tok = strtok(line, " ");
		assert(tok != NULL);
		A = atoi(tok);
		tok = strtok(NULL, " ");
		assert(tok != NULL);
		B = atoi(tok);
#ifdef VERBOSE_INPUT
		printf("%d %d\n", A, B);
#endif

		Numbers nums(A, B);
		printf("Case #%d: %d\n", (t+1), nums.result());
	}

	in.close();

	return 0;
}