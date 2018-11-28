#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <string.h>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#define inf 1000*1000*1000
#define mod 1000000009
#define ff first
#define ss second
#define mp make_pair
using namespace std;
int te, ind, x, n, m;
int main()
{
    freopen("D-small4.in", "r", stdin);
    freopen("D-small4.out", "w", stdout);
    scanf("%lld", &te);
    while(te--)
    {
        ind++;
        scanf("%d %d %d", &x, &n, &m);
        printf("Case #%d: ", ind);
        if(x==1)
        {
            printf("GABRIEL\n");
            continue;
        }
        if(x==2)
        {
            if(n%2==0 || m%2==0)
            {
                printf("GABRIEL\n");
            }
            else
            {
                printf("RICHARD\n");
            }
            continue;
        }
        if(x==3)
        {
            if((n%3==0 && m>=2) || (m%3==0 && n>=2))
            {
                printf("GABRIEL\n");
            }
            else
            {
                printf("RICHARD\n");
            }
            continue;
        }
        if(x==4)
        {
            if(n>=3 && m>=3 && n + m > 6)
            {
                printf("GABRIEL\n");
            }
            else
            {
                printf("RICHARD\n");
            }
            continue;
        }
    }
}
