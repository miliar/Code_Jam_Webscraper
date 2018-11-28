#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;
const int maxn=100+10;

int T, n, t[maxn];
char s[maxn];

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    scanf("%d", &T);
    for(int i=1; i<=T; i++)
    {
        scanf("%s", s);
        
        n=strlen(s);
        memset(t, 0, sizeof t);
        for(int j=n-1; j>=0; j--)
        {
            t[j]=t[j+1];
            if(s[j]=='+'&&!(t[j]&1))  continue;
            if(s[j]=='-'&& (t[j]&1))  continue;
            ++t[j];
        }
        printf("Case #%d: %d\n", i, t[0]);
    }
    return 0;
}
