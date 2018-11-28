//#include<bits/stdc++.h>
#include <cstdio>
#include <sstream>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <iostream>
#include <fstream>
#include <numeric>
#include <string>
#include <vector>
#include <cstring>
#include <map>
#include <iterator>

#define pb push_back
#define mp make_pair
#define ins insert
#define fi first
#define se second
#define ll long long int
#define sss stringstream
#define oss ostringstream
#define iss istringstream
#define llu long long unsigned

#define _sq(a) (a)*(a)
#define gcd(a,b)    __gcd(a,b)
#define lcm(a,b) ((a)*((b)/gcd(a,b)))
#define mem(a) memset(a, 0, sizeof(a))
#define _set(a) memset(a,-1,sizeof(a))
#define popcount(n) __builtin_popcount(n)
#define popcountl(n) __builtin_popcountll(n)
#define ctz(x) __builtin_ctz(x) //number of trailing zeroes in a digit
#define ctzl(x) __builtin_ctzll(x)
#define clz(x) __builtin_clz(n)
#define clzl(x) __builtin_clzll(x) //number of leading zeroes in a digit
//If Long Long (mask & (1LL << k))
#define check(mask, k) (mask & (1 << k))
#define set1(mask, k) (mask | (1 << k))
#define set0(mask ,k) (mask & (~(1<<k)))
#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)

using namespace std;
#define pi acos(-1.0)
#define mod 100000007
#define inf 1000000000
#define EPS 1e-9
#define MAX 100005
//int dx[] = {0,0,1,-1};
//int dy[] = {1,-1,0,0};
//int dx[] = {-1,-1,-1,0,0,1,1,1};
//int dy[] = {-1,0,1,-1,1,-1,0,1};
//typedef pair < int, int > pii;
bool vis[20];
int main()
{
    READ("A-small-attempt0.in");
    WRITE("output.txt");
    //ios_base::sync_with_stdio(false);
    int ncase, tcase, i, j, ans, a, cnt, num;
    scanf("%d", &ncase);
    for(tcase = 1; tcase <= ncase; tcase++)
    {
        mem(vis);
        scanf("%d", &ans);
        for(i = 1; i <= 4; i ++)
        {
            if(i == ans)
            {
                for(j = 1; j <= 4; j++)
                {
                    scanf("%d", &a);
                    vis[a] = 1;
                }
            }
            else
            {
                for(j = 1; j <= 4; j++) scanf("%d", &a);
            }
        }
        scanf("%d", &ans);
        cnt = 0;
        for(i = 1; i <= 4; i ++)
        {
            if(i == ans)
            {
                for(j = 1; j <= 4; j++)
                {
                    scanf("%d", &a);
                    if(vis[a])
                    {
                        cnt++;
                        num = a;
                    }
                }
            }
            else
            {
                for(j = 1; j <= 4; j++) scanf("%d", &a);
            }
        }
        printf("Case #%d: ", tcase);
        if(cnt == 0) printf("Volunteer cheated!\n");
        else if(cnt == 1) printf("%d\n", num);
        else printf("Bad magician!\n");
    }
    return 0;
}

