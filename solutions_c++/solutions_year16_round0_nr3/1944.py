#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <queue>
#include <set>
#include <climits>
using namespace std;

typedef long long ll;
int testCase;
ll n, k;

bool isCan(ll num)
{
    int cnt = 0;
    ll sum = -1;
    while(num)
    {
        sum += num%2;
        num >>= 1;
        sum *= -1;
        cnt++;
    }
    for(int i = 0; i < n -2 - cnt; i++)
        sum *= -1;
    if(sum == -1) return true;
    else return false;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("codeGem#C.out", "w+", stdout);
    scanf("%d", &testCase);
    for(int tc = 1; tc <= testCase; tc++)
    {
        printf("Case #%d:\n", tc);
        ll cnt = 0;
        scanf("%lld%lld", &n, &k);
        for(ll i = 0; i < (1 << (n-2)); i++)
        {
            if(isCan(i))
            {
                vector < ll > res;
                ll num = i;
                while(num)
                {
                    res.push_back(num % 2);
                    num >>= 1;
                }
                printf("1");
                for(int i = 0; i < res.size(); i++)
                    printf("%lld", res[i]);
                for(int i = 0; i < n-2-res.size(); i++)
                    printf("0");
                printf("1 ");
                
                for(int j = 2; j <= 10; j++)
                    printf("%d ", j+1);
                puts("");
                cnt++;
            }
            if(cnt == k) break;
        }
    }
}