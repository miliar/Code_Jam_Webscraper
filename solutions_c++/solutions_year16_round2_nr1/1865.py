#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <memory.h>
#include <cassert>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <queue>
#include <map>
#include <set>
#include <deque>
#include <bitset>
#include <cmath>

typedef unsigned int Ind;
typedef unsigned long long ull;

void solveCase(int iCase);
int main(int argc, char* argv[])
{
	using namespace std;

	freopen("input.in",   "r", stdin);
	freopen("output.out", "w", stdout);

	int nCases;
	scanf("%d", &nCases);

	for (int iCase = 1; iCase <= nCases; ++iCase)
	{
		solveCase(iCase);
	}
	return 0;
}


void solveCase(int iCase)
{
	char str[2000];
	scanf("%s", str);
	std::map<char, Ind> occur;
	for (Ind i = 0; i < 26; ++i) occur['A' + i] = 0;
	for (Ind i = 0; str[i] != '\0'; ++i)
	{
		++occur[str[i]];
	}
	Ind num[10];
	for (Ind i = 0; i < 10; ++i) num[i] = 0;
	// sift the zeroes
	for (Ind i = 0; i < occur['Z']; ++i) // z
	{
		++num[0];
		--occur['E']; --occur['R']; --occur['O'];
	}
	occur['Z'] = 0;
	// twos
	for (Ind i = 0; i < occur['W']; ++i)
	{
		++num[2];
		--occur['T']; --occur['O'];
	}
	occur['W'] = 0;
	// sixs
	for (Ind i = 0; i < occur['X']; ++i)
	{
		++num[6];
		--occur['S']; --occur['I'];
	}
	occur['X'] = 0;
	// sevens
	for (Ind i = 0; i < occur['S']; ++i)
	{
		++num[7];
		--occur['E']; --occur['V']; --occur['E']; --occur['N'];
	}
	occur['S'] = 0;
	// fours
	for (Ind i = 0; i < occur['U']; ++i)
	{
		++num[4];
		--occur['F']; --occur['O']; --occur['R'];
	}
	occur['U'] = 0;
	//
	for (Ind i = 0; i < occur['R']; ++i)
	{
		++num[3];
		--occur['T']; --occur['H']; --occur['E']; --occur['E'];
	}
	for (Ind i = 0; i < occur['T']; ++i)
	{
		++num[8];
		--occur['E']; --occur['I']; --occur['G']; --occur['H'];
	}
	for (Ind i = 0; i < occur['O']; ++i)
	{
		++num[1];
		--occur['N']; --occur['E'];
	}
	for (Ind i = 0; i < occur['V']; ++i)
	{
		++num[5];
		--occur['F']; --occur['I']; --occur['E'];
	}
	for (Ind i = 0; i < occur['N'] / 2; ++i)
	{
		++num[9];
	}

	printf("Case #%d: ", iCase);
	for (Ind i = 0; i < 10; ++i)
	{
		for (Ind j = 0; j < num[i]; ++j)
			printf("%d", i);
	}
	printf("\n");
}
