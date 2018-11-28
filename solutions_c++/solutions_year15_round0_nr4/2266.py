#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <algorithm>
#include <iomanip>
#include <queue>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <stack>
#include <bitset>
#include <sstream>
#include <fstream>

typedef unsigned long long ull;
#define mp make_pair
#define pb push_back

const long double eps = 1e-9;
const double pi = acos(-1.0);
const long long inf = 1e18;
const int inf2 = 10000;
using namespace std;

int f1(int a, int b)
{
    if (a == b)
        return -1;
    int chelsea = a * b;
    if (chelsea >-2 && chelsea < 2)
        return chelsea;
    if(a>b) chelsea = -chelsea;
    if (chelsea == 2) return 2;
    else if (chelsea == 3) return 3;
    else if (chelsea == 5) return 5;
    else if (chelsea == -2) return -2;
    else if (chelsea == -3) return  -3;
    else if (chelsea == -5) return  -5;
    else if (chelsea == -6) return  -5;
    else if (chelsea == -15) return  -2;
    else if (chelsea == -10) return  -3;
    else if (chelsea == 6) return 5;
    else if (chelsea == 15) return  2;
    else if (chelsea == 10) return  3;
}

int main (int argc, const char * argv[])
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int j = 1; j <= T; ++j)
    {
        int x, r, s;
        scanf("%d%d%d", &x, &r, &s);
        if (x == 1)
            printf("Case #%d: GABRIEL\n", j); // +
        else if (x == 2)
        {
            if((r==1 && s==1) || (r==1 && s==3) || (r==3 && s==1) || (r==3 && s==3))
                printf("Case #%d: RICHARD\n", j);
            else
                printf("Case #%d: GABRIEL\n", j);
        }
        else if (x == 3)
        {
            if ((r==1 || s==1) || (s==2 && r==2) || (r==2 && s==4)||(r==4 && s==2) || (r==4 && s==4))
                printf("Case #%d: RICHARD\n", j);
            else
                printf("Case #%d: GABRIEL\n", j);
        }
        else if (x == 4)
        {
            if((r==3 && s==4)|| (r==4 && s==3) || (r==4 && s==4))
                printf("Case #%d: GABRIEL\n", j);
            else
                printf("Case #%d: RICHARD\n", j);
        }
        //for (int k = 0; k < D; ++k)
          //  cout << v[k] << " ";
        //cout << endl;
    }
    return 0;
}
