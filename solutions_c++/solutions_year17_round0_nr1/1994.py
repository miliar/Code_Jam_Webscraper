#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/stack:16777216")
#include <string>
#include <vector>
#include <map>
#include <list>
#include <iterator>
#include <set>
#include <queue>
#include <iostream>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <utility>
#include <time.h>

#include <fstream>
#include <sys/stat.h>
#include <stdlib.h>
#include <stdio.h>
using namespace std;

#define FOR(i, a, b) for(int i=(a);i<(b);i++)
#define RFOR(i, b, a) for(int i=(b)-1;i>=(a);--i)
#define FILL(A,value) memset(A,value,sizeof(A))
#define ALL(V) V.begin(), V.end()
#define SZ(V) (int)V.size()
#define PB push_back
#define MP make_pair
#define Pi 3.14159265358979

typedef long long Int;
typedef unsigned long long UInt;
typedef vector<int> VI;
typedef pair<int, int> PII;



int main()
{
    freopen("in.txt", "r" , stdin);
    freopen("out.txt" , "w" , stdout);


    int t;
    cin >> t;
    FOR(tt,0,t)
    {
        printf("Case #%d: ", tt + 1);
        string s;
        int k;
        cin >> s >> k;
        int res = 0;
        FOR(i,0,SZ(s) - k + 1)
        {
            if (s[i] == '-')
            {
                ++ res;
                FOR(j,0,k)
                {
                    if (s[i + j] == '-') s[i + j] = '+';
                    else s[i + j] = '-';
                }
            }
        }
        FOR(i,0,SZ(s))
            if (s[i] == '-')
                res = -1;

        if (res == -1)
        {
            cout << "IMPOSSIBLE" << endl;
        }
        else
        {
            cout << res << endl;
        }

    }

    return 0;
}
