#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("file.in");
ofstream fout("file.out");

typedef unsigned long long ull;

ull mote[150];

int size;


int compare (const void * a, const void * b)
{
	if (*(ull*)a < *(ull*)b)
		return -1;
	if (*(ull*)a > *(ull*)b)
		return 1;
	return 0;
}

int sum(int pos, ull &curArmin)
{
	if (curArmin <= 1)
		return -1;
	ull cur = curArmin - 1;
	int result = 0;
	while (mote[pos] >= curArmin)
	{
		curArmin += cur;
		cur = cur * 2;
		result ++;
	}

	return result;
}

int minResult = 0;

int Solve (int startPos, ull armin, int result)
{
	int r;
	for (r = startPos; r < size; r++)
	{
		if (mote[r] < armin)
		{
			armin += mote[r];
		} else {
			if (result < minResult)
			{
				// remove
				int result1 = Solve(r+1, armin, result+1);
				
				// add
				int temp  = sum(r, armin);
				if (temp == -1)
					return result1;

				int result2 = Solve(r, armin, result+temp);
				
				if (result1 > result2)
					return result2;
				else 
					return result1;
			} else {
				return minResult;
			}
		}
	}
	return result;
}




int main()
{
	int n;
	int i, r;
	int result = 0;
	ull armin;
	
	fin >> n;
	for (i = 0; i < n; i++)
	{
		result = 0;
		fin >> armin >> size;
		for (r = 0; r < size; r++)
		{
			fin >> mote[r];
		}

		qsort(mote, size, sizeof(ull), compare);

		for (r = 0; r < size; r++)
		{
			if (mote[r] < armin)
			{
				armin += mote[r];
			} else {
				break;
			}
		}
		minResult  = size - r;
		
		result = Solve(r, armin, 0);

		fout << "Case #" << (i+1) << ": " << result << endl;
	}

	return 0;
}