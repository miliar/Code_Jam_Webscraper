#include<cstdlib>
#include<cctype>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>
#include<string>
#include<map>
#include<iostream>
#include<sstream>
#include<fstream>
#include<bitset>
#include<list>
using namespace std;

const double EPS = 0.00000001;

int main()
{

    //freopen("E:\\A-large.in", "r", stdin);
    //freopen("E:\\A-large.out", "w", stdout);

    int T;

    scanf("%d", &T);

    for (int cas = 0; cas < T; cas++)
    {
        int n = 0;
        char str[1002];

        int sum = 0;
        int count = 0;

        scanf("%d %s", &n, &str);

        for(int i = 0; i <= n; ++i)
        {
            int t = (int) str[i] - '0' ;

            if(t == 0 )
                continue;

            if(i > sum) {
                count += (i - sum);
                sum += (i - sum);
            }

            sum += t;
        }
        printf("Case #%d: %d\n", cas + 1, count);
    }

    return 0;
}

