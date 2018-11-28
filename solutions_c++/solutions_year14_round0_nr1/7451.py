#include <iostream>
#include <map>
#include <vector>
#include <list>
#include <set>
#include <fstream>
using namespace std;


int main(int argc, char **argv)
{
	FILE *fptr = fopen("input.txt", "r");
	if (fptr == 0) return 1;
	FILE *outPtr = fopen("output.txt", "w");
	if (outPtr == 0) return 1;
	int T;
	fscanf(fptr, "%d", &T);
	for (int a = 0; a < T; a++)
	{
		int firstAns = 0;
		fscanf(fptr, "%d", &firstAns);
		set<int> firstSet;
		for (int i = 0; i < 4; i++)
		{
			int a, b, c, d;
			fscanf(fptr, "%d %d %d %d", &a, &b, &c, &d);
			if (i == firstAns-1)
			{
				firstSet.insert(a);
				firstSet.insert(b);
				firstSet.insert(c);
				firstSet.insert(d);
			}
		}

		int secondAns = 0;
		fscanf(fptr, "%d", &secondAns);
		int matches = 0;
		int match = 0;
		int arr2[4];
		for (int i = 0; i < 4; i++)
		{
			int a, b, c, d;
			fscanf(fptr, "%d %d %d %d", &a, &b, &c, &d);
			if (i == secondAns-1)
			{
				arr2[0] = a;arr2[1] = b;arr2[2] = c; arr2[3] = d;
			}
		}
		
		for (int i = 0; i < 4; i++)
			if (firstSet.count(arr2[i]))
			{
				matches++;
				match = arr2[i];
			}
			
		if (matches == 1) 
		{
			fprintf(outPtr, "Case #%d: %d\n", a+1, match);
		}
		else if (matches == 0)
		{
			fprintf(outPtr, "Case #%d: Volunteer cheated!\n", a+1);
		}
		else
		{
			fprintf(outPtr, "Case #%d: Bad magician!\n", a+1);
		}
	}
	return 0;
}