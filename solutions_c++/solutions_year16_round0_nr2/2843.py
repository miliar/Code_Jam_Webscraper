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
		char c[102] = {'\0'};
        fin >> c;

		bool b[102];
		for (int i = 0; i < 102; i++)
		{
			b[i] = true;
		}
		for (int i = 0; i < strlen(c); i++)
		{
			if (c[i] == '+')
			{
				b[i] = true;
			}
			else
			{
				b[i] = false;
			}
		}

		int count = 0;
		while (1)
		{
			for (int i = 0; i < strlen(c); i++)
			{
				if ((b[i] == false && b[i + 1] == true)
					|| (b[i] == true && b[i + 1] == false))
				{
					for (int k = 0; k <= i; k++)
					{
						if (b[k] == true)
						{
							b[k] = false;
						}
						else
						{
							b[k] = true;
						}
					}
					count++;
					break;
				}
			}

			int num = 0;
			for (int i = 0; i < strlen(c); i++)
			{
				if (b[i] == false)
				{
					num++;
				}
			}
			if (num == strlen(c))
			{
				count++;
				break;
			}
			else if (num == 0)
			{
				break;
			}

			//if (b[0] == true && b[1] == true && b[2] == true && b[3] == true && b[4] == true &&
			//	b[5] == true && b[6] == true && b[7] == true && b[8] == true && b[9] == true)
			//{
			//	break;
			//}
		}

		fout << "Case #" << j + 1 << ": " << count << endl;
    }
	
    return (0);
}
