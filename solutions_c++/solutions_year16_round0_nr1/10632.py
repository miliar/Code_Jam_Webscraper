#include <iostream>
#include <cstdio>
#include <algorithm>
#include <stdlib.h>
#include <cstring>
using namespace std;
const long long MX = 1e18;
int num[105];
int main()
{
    int t;
    cin >> t;
    int cas = 1;
    while(t--)
    {
        long long m;
        cin >> m;
        long long n = m;
        memset(num, 0, sizeof(num));
        bool flag = false;
        if(n == 0)
        {
            printf("Case #%d: ", cas++);
            puts("INSOMNIA");
            continue;
        }
        for(int i = 0; i < 1000000; i++)
        {
            long long temp = n;
            while(temp)
            {
                num[temp % 10]++;
                temp /= 10;
            }
            int sum = 0;
            for(int j = 0; j < 10; j++)
            {
                if(num[j] > 0)
                    sum++;
            }
            if(sum == 10)
            {
                flag = true;
                break;
            }
            n += m;
 
        }
        printf("Case #%d: ", cas++);
        if(flag)
            cout << n << endl;
        else
            puts("INSOMNIA");
    }
}
