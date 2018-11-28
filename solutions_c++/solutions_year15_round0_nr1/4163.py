#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <fstream>
#include <vector>

using namespace std;

int acc[1024];
char ss[1024];
int main(int argc, char* argv[])
{
	FILE* pf_in = fopen("A-large.in", "r");
	FILE* pf_out = fopen("lout", "w");
	int T;
	fscanf(pf_in, "%d", &T);
	for(int i = 1; i <= T; i++)
	{
		int S;
		fscanf(pf_in, "%d", &S);
		//cout << S << " ";

		fscanf(pf_in, "%s", ss);
		//cout << ss << endl;
		acc[0] = ss[0] - '0';
		int f = 0;
		for(int j = 1; j <= S; j++)
		{
			if(j > acc[j - 1])
			{
				f += j - acc[j - 1];
				acc[j] = j + ss[j] - '0';
			}
			else
			{
				acc[j] = acc[j - 1] + ss[j] - '0';
			}
		}
		fprintf(pf_out, "Case #%d: %d\n", i, f);
	}
	return 0;
}

