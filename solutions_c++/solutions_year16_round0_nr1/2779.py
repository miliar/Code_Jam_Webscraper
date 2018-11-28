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
    for (long long j = 0; j < T; j++)
    {
        long long N;
        fin >> N;

		bool b[10] = { false };

		long long n = N;
		while (1)
		{
			for (long long i = n; i > 0; i /= 10)
			{
				long long d = i % 10;
				b[d] = true;
			}

			if (b[0] == true && b[1] == true && b[2] == true && b[3] == true && b[4] == true &&
				b[5] == true && b[6] == true && b[7] == true && b[8] == true && b[9] == true)
			{
				break;
			}
			else if (n == 0)
			{
				break;
			}

			n += N;
		}

		if (n == 0)
		{
			fout << "Case #" << j + 1 << ": " << "INSOMNIA" << endl;
		}
		else
		{
			fout << "Case #" << j + 1 << ": " << n << endl;
		}
    }
	
    return (0);
}
