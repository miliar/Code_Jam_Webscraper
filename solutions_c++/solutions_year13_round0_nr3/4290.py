#include<stdio.h>
#include<iostream>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<algorithm>
#include<set>
#include<map>
#include<utility>
#include<vector>
#include<string>
#include<stack>
#include<queue>
using namespace std;
long long pals[46];
int check(long long x)
{
    int num[9],i=0,j;
    while(x)
    {
        num[i++] = x%10;
        x /= 10;
    }
    j = i-1;
    for (i=0; i<j; ++i,--j)
    {
        if (num[i] != num[j]) return false;
    }
    return true;
}
int main()
{
    //freopen("inputClarge.in", "r", stdin);
    //freopen("Cout.txt", "w", stdout);
    int i,P,count;
    int t,T;
    long long x,A,B;
    for (i=1,P=1; i<=10000000; ++i)
    {
        x = (long long) i * (long long) i;
        if (check(i) && check(x)) pals[P++] = x;//, printf("%d %lld\n", i,x);
    }
    /*printf("size : %d\n", P);
    for (i=0; i<P; ++i) printf("%lld\n",pals[i]);*/
    scanf("%d", &T);
    for (t=1; t<=T; ++t)
    {
        scanf("%lld %lld", &A, &B);
        count = 0;
        for (i=0; i<P; ++i)
        {
            if (pals[i]>=A && pals[i]<=B) ++count;
        }
        printf("Case #%d: %d\n", t, count);
    }
    return 0;
}
