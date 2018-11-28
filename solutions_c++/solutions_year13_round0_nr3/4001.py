#include<algorithm>
#include<iostream>
#include<fstream>
#include<cstdio>
#include<vector>
#include<fstream>
#include<iomanip>
#include<bitset>
#include<deque>
#include<string>
#include<map>
#include<cstring>
#include<sstream>
#include<cmath>
using namespace std;

typedef unsigned long long ULL;

#define MAX 10000000

vector<ULL> squareAndFair; 

bool palindrome (ULL num)
{
	string numStr;
	stringstream ss;
	ss << num;
	numStr = ss.str ();
	int i = 0;
	int j = numStr.size ()-1;
	while (i < j)
	{
		if (numStr[i] == numStr[j])
		{
			i++;
			j--;
		}
		else
			return false;
	}
	return true;
}

void precalc ()
{
	for (int i = 1; i <= MAX; i++)
	{
		if (palindrome ((ULL)i))
		{
			ULL square = (ULL)i*(ULL)i;
			if (palindrome (square))
				squareAndFair.push_back (square);
		}
	}
}

int main()
{
	precalc ();
	FILE *fp = fopen ("input", "r");
	FILE *fp1 = fopen ("output", "w");
	int T;
	fscanf (fp, "%d", &T);
	for (int t = 0; t < T; t++)
	{
		ULL A, B;
		fscanf (fp, "%llu %llu", &A, &B);
		int count  = 0;
		for (int i = 0; i < squareAndFair.size (); i++)
		{
			if (squareAndFair[i] >= A && squareAndFair[i] <= B)
				count++;
		}
		fprintf (fp1, "Case #%d: %d\n", (t+1), count);
	}
	return 0;
}
