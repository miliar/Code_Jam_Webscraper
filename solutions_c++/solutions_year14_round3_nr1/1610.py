#include <iostream>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <utility>
#include <locale>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <climits>
#include <cfloat>
#include <map>
#include <functional>
using namespace std;
const double PI = acos(0.0) * 2.0;

FILE* output;
long long numer, denom, two_[42];

long long GCD(long long sml, long long bg)
{
    if(sml>bg) swap(sml, bg);
    while(sml)
    {
        bg %= sml;
        swap(sml, bg);
    }
    return bg;
}

int main() // Google Code Jam 2014 Round 1C
{
    output = fopen("myOutput.txt", "w");

    for(int i=0; i<42; i++) two_[i] = 1<<i; // 2의 거듭제곱

    int tc_N;
    scanf("%d", &tc_N);

    for(int tc=1; tc<=tc_N; tc++)
    {
        scanf("%lld/%lld", &numer, &denom);

        long long gcd = GCD(numer, denom);

        numer /= gcd;
        denom /= gcd;

        bool valid = false;

        for(int i=0; i<41; i++)
            if(denom == two_[i])
            {
                valid = true;
                break;
            }

        if(!valid) fprintf(output, "Case #%d: impossible\n", tc);
        else
        {
            int cnt;
            for(cnt=0; numer < denom; cnt++) denom >>= 1;

            fprintf(output, "Case #%d: %d\n", tc, cnt);
        }
    }

    fclose(output);

    return 0;
}