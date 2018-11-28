#include <vector>
#include <algorithm>
#include <fstream>
#include <string>

using namespace std;

ifstream ein;
FILE * aus;
int TestCase;

#define E 0
#define I 1
#define J 2
#define K 3
#define mE 4
#define mI 5
#define mJ 6
#define mK 7

// 1 i j k -1 -i -j -k
// 0 1 2 3  4  5  6  7

// right multiplication tables
int i[8] = {I, mE, mK, J, mI, E, K, mJ};
int j[8] = {J, K, mE, mI, mJ, mK, E, I};
int k[8] = {K, mJ, I, mE, mK, J, mI, E};

void start()
{
	printf("%d\n", TestCase);
	string result;
	// read test case
	int L, X;
	ein >> L >> X;
	string s;
	ein >> s;
	int e = 0;
	int p = 0;
	for (int xx = 1; xx <= X; xx++)
	{
		for (int sx = 0; sx < s.length(); sx++)
		{
			if (s[sx] == 'i')
				p = i[p];
			if (s[sx] == 'j')
				p = j[p];
			if (s[sx] == 'k')
				p = k[p];

			if ((e == 0) && (p == I))	// I
			{
				e++;
			}
			if ((e == 1) && (p == K))   // IJ
			{
				e++;
			}
		}
	}
	if ((e == 2) && (p == mE))			// IJK
	{
		result = "YES";
	}
	else
	{
		result = "NO";
	}

	// output result
	fprintf(aus, "Case #%d: %s\n", TestCase, result.c_str());     // %llu , %ll
}

void main()
{
	int NumTestCases;	
	ein.open("C-small-attempt0.in");
	aus = fopen("ausgabe.txt","w");
	
	ein >> NumTestCases;
	for (TestCase = 1; TestCase <= NumTestCases; TestCase++)
		start();

	fclose(aus);
	ein.close();
}
