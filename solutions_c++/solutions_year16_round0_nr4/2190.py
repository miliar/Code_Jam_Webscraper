#include <cstdio>
#include <vector>
#include <deque>
#include <queue>
#include <map>
#include <algorithm>
#include <functional>
#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <string.h>

using namespace std;

int main(int argc, const char **argv)
{
    if (argc != 2)
    {
        fprintf(stderr, "Error:%d\n", __LINE__);
        return -1;
    }

    ifstream fin(argv[1]);
    ofstream fout("out.txt");

    int T;
    fin >> T;
    for (int j = 0; j < T; j++)
    {
        int K;
        fin >> K;
		int C;
		fin >> C;
		int S;
		fin >> S;

		fout << "Case #" << j + 1 << ":";
		for (int i = 0; i < S; i++)
		{
			fout << " " << i + 1;
		}
		fout << endl;
    }
	
    return (0);
}
