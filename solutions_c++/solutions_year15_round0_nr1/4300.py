#include <iostream>
#include <iomanip>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <stack>
#include <queue>
#include <string>
#include <cstdlib>
#include <set>
#include <map>
#include <fstream>
#include <bitset>

#define PI 3.14159265359

using namespace std;


int main()
{
    freopen("p1.in", "r", stdin);
    freopen("p1.out", "w", stdout);
    int tc;
    scanf("%d", &tc);
    for(int kras=1; kras<=tc; kras++)
    {
        int s_max;
        string people;
        scanf("%d", &s_max);
        cin >> people;

        int total_sum=people[0]-'0';
        int added=0;
        for(int i=1; i<s_max+1; i++)
        {
            if(total_sum >= i)
            {
                total_sum += people[i]-'0';
            }
            else
            {
                added += i-total_sum;
                total_sum = i;
                total_sum += people[i]-'0';
            }
        }
        printf("Case #%d: %d\n", kras, added);

    }
    return 0;
}
