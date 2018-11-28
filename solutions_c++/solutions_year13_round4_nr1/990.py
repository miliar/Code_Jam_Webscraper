#include <cstdlib>
#include <cstdio>
#include <vector>
#include <string>
#include <memory.h>
#include <algorithm>

using namespace std;

const char inFileName[] = "A-small.in";
const char outFileName[] = "A-small.out";

const int MOD = 1000002013;
const int MaxM = 2020;

int T;
int n, m;
long long sol;

struct Point
{
	long long x;
	long long val;
	int start;
	Point() {}
};

bool cmp(const Point& A, const Point& B)
{
	if (A.x != B.x)
		return (A.x < B.x);
	return (A.start < B.start);
}

Point points[2 * MaxM];
Point myStack[2 * MaxM];

int main() {
	
	FILE* inFile = fopen(inFileName, "r");
	FILE* outFile = fopen(outFileName, "w");

	fscanf(inFile, "%d", &T);
	for (int t = 0; t < T; t++) 
	{
		fscanf(inFile, "%d%d\n", &n, &m);

		long long currVal = 0LL;
		for (int i = 1; i <= m; i++)
		{
			int x, y, z;
			fscanf(inFile, "%d%d%d", &x, &y, &z);
			points[i].x = x;
			points[i].val = z;
			points[i].start = 0;
			points[i + m].x = y;
			points[i + m].val = z;
			points[i + m].start = 1;
			
			long long x1 = x, y1 = y, z1 = z;
			long long sum = (((y - x) * (y - x + 1)) / 2) % MOD;
			sum = (sum * z) % MOD;
			currVal = (currVal + sum) % MOD;
		}
		sort(points + 1, points + 2 * m + 1, cmp);

		long long newVal = 0LL;
		int stackSize = 0;
		for (int i = 1; i <= 2 * m; i++)
		{
			if (points[i].start == 0)
			{
				myStack[++stackSize] = points[i];
			}
			else
			{
				int val = points[i].val;
				while (val > 0)
				{
					Point point = myStack[stackSize];
					if (point.val >= val)
					{
						long long sum = (((points[i].x - point.x) * (points[i].x - point.x + 1)) / 2) % MOD;
						sum = (sum * val) % MOD;
						newVal = (newVal + sum) % MOD;
						myStack[stackSize].val -= val;
						val = 0;
					}
					else
					{
						long long sum = (((points[i].x - point.x) * (points[i].x - point.x + 1)) / 2) % MOD;
						sum = (sum * point.val) % MOD;
						newVal = (newVal + sum) % MOD;
						val -= point.val;
						stackSize--;
					}
				}
			}
		}

		long long sol = (newVal - currVal) % MOD;
		if (sol < 0) sol += MOD;
		fprintf(outFile, "Case #%d: %lld\n", t + 1, sol);
	}	
	
	fclose(inFile);
	fclose(outFile);
	return 0;
}
