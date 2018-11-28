#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>
#include <iostream>
#include <cstdlib>

using namespace std;

bool isPar(long long a)
{
    long long orig = a;
    if (a < 10)
        return true;
    long long res = 0;
    while (a > 0)
	{
        res = res * 10 + a % 10;
        a = a / 10;
	}
    if (res == orig)
        return true;
	else
        return false;
}

map<long long, long long> sq;

int main()
{

	int T;

    for (long long i = 1; i <= 10000; i++)
	{
        long long res = i * i;
        sq[res] = i;
	}


    ifstream fin("C:\\weilin\\Competition\\codeForces\\CodeJam2013\\CodeJam2013\\C-small-attempt0.in");

    //ifstream fin("C:\\weilin\\Competition\\codeForces\\CodeJam2013\\CodeJam2013\\test.txt");

     ofstream fout("C:\\weilin\\Competition\\codeForces\\CodeJam2013\\CodeJam2013\\output.txt");

	fin >> T;
	
    
	for (int i=0; i <T; i++)
	{
        long long N, M;
        fin >> N >> M;
        long long total = 0;
        for (long long j = N; j <= M; j++)
		{
            if (isPar(j))
			{
                if (sq.find(j) != sq.end())
				{
                    long long root = sq[j];
                    if (isPar(root))
                        total ++;
				}
			}
		}


        fout << "Case #" << i+1 <<  ": "<< total << endl; 

	}
	return 0;
}