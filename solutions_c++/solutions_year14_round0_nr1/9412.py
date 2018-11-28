#include <iostream>
#include <cstdio>
#include <string>
#include <sstream>
using namespace std;

#define FOR(i, a, n) for((i)=0;(i)<(int)(n);(i)++)
int i, j, k, n, in;
char c;

int m1[4][4], m2[4][4], a1[4], a2[4], r1, r2, match, result;

template <typename T>
string NumberToString ( T Number )
{
    ostringstream ss;
    ss << Number;
    return ss.str();
}

void readrow1()
{
	scanf("%d", &r1);
	r1 = r1-1;
}

void readrow2()
{
	scanf("%d", &r2);
	r2 = r2-1;
}

void readmap1()
{
	FOR(i, 0, 4)
	{
		FOR(j, 0, 4)
		{
			scanf(" %d ", &m1[i][j]);
		}
	}
}

void readmap2()
{
	FOR(i, 0, 4)
	{
		FOR(j, 0, 4)
		{
			scanf(" %d", &m2[i][j]);
		}
	}
}

void geta1()
{
	FOR(i, 0, 4)
	{
		a1[i] = m1[r1][i];
	}
}

void geta2()
{
	FOR(i, 0, 4)
	{
		a2[i] = m2[r2][i];
	}
}

void comparea1a2()
{
	match = 0;

	FOR(i, 0, 4)
	{
		FOR(j, 0, 4)
		{
			if (a1[i] == a2[j])
			{
				match++;
				result = a1[i];
			}
		}
	}
}

void output(int case_no)
{
	printf("Case #%d: ", case_no+1);

	if (match == 1)
	{
		printf("%d", result);
	}
	else if (match > 1)
	{
		printf("Bad magician!");
	}
	else
	{
		printf("Volunteer cheated!");
	}

	printf("\n");
}

void main()
{
	freopen("a.in", "r", stdin);
	freopen("output.txt","w",stdout);

	scanf("%d", &n);
	
	FOR(in, 0, n)
	{
		readrow1();
		readmap1();
		geta1();
		readrow2();
		readmap2();
		geta2();

		comparea1a2();
		output(in);
	}
}