#include <string>
#include <cctype>
#include <vector>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <numeric>
#include <cstdlib>
#include <cstdio>
#include <queue>
#include <stack>
#include <memory.h>
#include <assert.h>
#include "bigint/BigIntegerLibrary.hh"
using namespace std;


int main(void)
{

	FILE *inf;
	FILE *outf;
	inf = fopen("A-small.in", "r");
	outf = fopen("aout.out","w");
	int nTest;
	int radius, t;
	int res;
	char line[128];
	fgets(line, 128, inf);
	nTest = atoi(line);

	for (int i = 0; i < nTest ; i++)
	{
		fgets(line, 128, inf);
		string tmp(line);
		int pos = tmp.find_first_of(' ');
		string radi = tmp.substr(0, pos);
		string lit = tmp.substr(pos+1, tmp.length()-pos-2);
		BigInteger radiBig = stringToBigInteger(radi);
		BigInteger litBig = stringToBigInteger(lit);
		BigInteger result = 0;
		BigInteger tmpBig = 0;
		BigInteger consumed = 0;
		tmpBig = radiBig*2+1;

		while (consumed <= litBig)
		{
			consumed += tmpBig;
			tmpBig += 4;
			result++;
		}
		string ressting = bigIntegerToString(result-1);
		fprintf(outf, "Case #%d: %s\n", i+1, ressting.c_str());
	}
	return 1;
}