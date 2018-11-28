#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <unordered_set>
#include <map>
#include <fstream>

using namespace std;

int T, R, N;
int main()
{
	string filename = "A-small-attempt1";
	ifstream fin(filename + ".in");
	FILE *fout = fopen((filename + ".out").c_str(), "w");

	fin >> T;
	for(int i = 0; i < T; i++)
	{
		int v[17] = {};
		for(int j = 0; j < 2; j++)
		{
			fin >> R;
			for(int k = 1; k <= 4; k++)
			{
				for(int l = 1; l <= 4; l++)
				{
					fin >> N;
					if(k == R)
					{
						v[N]++;
					}
				}
			}
		}

		int c = 0;
		for(int j = 0; j < 17 && c != -1; j++)
		{
			if(v[j] == 2)
			{
				if(c == 0)
				{
					c = j;
				}
				else
				{
					c = -1;
				}
			}
		}

		string res = "";
		if(c == -1)
		{
			fprintf(fout, "Case #%d: %s\n", i + 1, "Bad magician!");
		}
		else if(c == 0)
		{
			fprintf(fout, "Case #%d: %s\n", i + 1, "Volunteer cheated!");
		}
		else
		{
			fprintf(fout, "Case #%d: %d\n", i + 1, c);
		}
	}

	fin.close();
	fclose(fout);
 	return 0;
}