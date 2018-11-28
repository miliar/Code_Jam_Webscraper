#include <iostream>
#include <vector>
#include <cmath>
#include <cstdio>
#include <set>
#include <map>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>

#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define ll long long

using namespace std;

int main()
{
    int T;
    scanf("%d", & T);

    for (int t = 0; t < T; t++)
    {
        int x, y;
        scanf("%d%d", & x, & y);
        printf("Case #%d: ", t + 1);

        for (int i = 0; i < abs(x); i++)
        {
            if (x < 0)
                printf("EW");
            else
                printf("WE");
        }

        for (int i = 0; i < abs(y); i++)
        {
            if (y < 0)
                printf("NS");
            else
                printf("SN");
        }
        printf("\n");
    }
}
