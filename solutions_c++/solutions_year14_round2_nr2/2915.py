#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
#include <cctype>
#include <locale>

using namespace std;

int main(int argc, const char *argv[])
{
	string inputFileName = "B-small-attempt1.in";
	string outputFileName = "output.txt";
	freopen(inputFileName.c_str(), "r", stdin);
	freopen(outputFileName.c_str(), "w", stdout);

    long long test, A, B, K, C;
    long long l, i, j, m, chk;

    scanf("%lld",&test);

    for(m = 1; m<=test; m++)
    {
        scanf("%lld%lld%lld",&A,&B,&K);

        chk = 0;

        for(i = 0; i<=A-1;i++)
        {
            for(j = 0; j<=B-1; j++)
            {
                C = i&j;
                if(C < K)
                {
                    chk = chk + 1;
                }

            }
        }

        printf("Case #%lld: %lld\n",m,chk);
    }
    return 0;
}
