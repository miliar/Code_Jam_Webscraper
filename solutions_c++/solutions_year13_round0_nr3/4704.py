#include <iostream>
#include <stdio.h>
using namespace std;
bool huiwen(long long int x)
{
    char str[50];
    int s=0;
    while(x)
    {
        str[s++] = x%10;
        x/=10;
    }
    for(int i=0;i<s;i++)
        if(str[i]!=str[s-1-i]) return false;
    return true;
}
int main()
{
    //freopen("c:\\codejam\\C-small-attempt0.in","r",stdin);
    //freopen("c:\\codejam\\C-small-attempt0.out","w",stdout);
    int out = 0;
    int num=0;
    long long int table[100];
    for(int i=1;i<=10000000;i++)
        if(huiwen(i))
        {
            if(huiwen((long long int )i*i))
                table[++num] = (long long int)i*i;
        }
    int T;
    scanf("%d",&T);
    while(T--)
    {
        long long int A,B;
        cin>>A>>B;
        int s=0;
        while(table[++s] < A);
        int e=0;
        while(table[++e] <= B);
        printf("Case #%d: %d\n",out++,e-s);
    }
    return 0;
}
