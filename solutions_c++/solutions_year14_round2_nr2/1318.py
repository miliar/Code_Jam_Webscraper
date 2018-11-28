#include <iostream>
#include <fstream>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <climits>
#include <vector>
#include <algorithm>
#include <map>
typedef long long ll;
using namespace std;
const int N = 101;
int a = 0;
int b = 0;
int k = 0;
inline int solve()
{
	int i = 0; 
	int j = 0;
	int cnt = 0;
	for(i = 0; i < a; ++i)
	{
		for(j = 0; j < b; ++j)
		{
			if((i & j) < k)
			{
				cnt += 1;
			}
		}
	}
	return cnt;
}
int main()
{
	int t = 0;		
	int i = 0, j = 0;
	char buffer[2048];

	FILE* in = freopen("D:/Lab/Contests/Contests/file/B-small-attempt0.in", "r", stdin);
	FILE* out = freopen("D:/Lab/Contests/Contests/file/B-small-attempt0.out", "w", stdout);

	fscanf(in, "%d", &t);

	for(i = 0; i < t; i++)
	{
		fscanf(in, "%d %d %d", &a, &b, &k);

		fprintf(out, "Case #%d: %d\n", (i + 1), solve());
	}

	fclose(out);
	fclose(in);

	return 0;
}