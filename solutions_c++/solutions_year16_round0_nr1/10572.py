#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<iostream>
#include<algorithm>
#include<queue>
#include<stack>
#include<vector>
#include<map>
#include<set>
#include<deque>
#include<bitset>
#include<time.h>
#define ll long long
#define inf 0x7FFFFFFF
#pragma comment(linker, "/STACK:102400000,102400000")
using namespace std;
bool checkNum[15];
ll sum;
int countDigit;
bool add(ll x)
{
    if (checkNum[x] == false)
    {
        countDigit++;
        checkNum[x] = true;
        if (countDigit >= 10)
            return true;
    }
    return false;
}
bool deal()
{
    ll now = sum;
    if (now == 0)
    {
        return add(0);
    }
    while (now)
    {
        if (add(now%10)) return true;
        now/=10;
    }
    return false;
}
int main()
{
    int i,j,k;
    int m,t;
    ll n;
    //srand((unsigned)time(NULL));//int data=rand()%10000+1;
    freopen("A-large.in","r",stdin);freopen("A-large-output.txt","w",stdout);
    scanf("%d",&t);
    for(int tcase=1;tcase<=t;tcase++)
    //while(scanf("%d",&n)!=EOF)
    {
        //cout<<tcase<<endl;
        scanf("%lld", &n);
        if (n == 0)
        {
            printf("Case #%d: INSOMNIA\n",tcase);
            continue;
        }
        memset(checkNum,0,sizeof(checkNum));
        countDigit = 0;
        sum = 0;
        while (true)
        {
            sum += n;
            if (deal()) break;
        }
        printf("Case #%d: %lld\n",tcase, sum);
    }
}
