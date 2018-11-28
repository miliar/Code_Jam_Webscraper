#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

const int MAXN=1010;

int n,rj;

char s[MAXN];

int main()
{
    int test;
    scanf("%d",&test);
    for(int br=0;br<test;br++)
    {
        rj=0;
        scanf("%d",&n);
        scanf("%s",s);
        int sad=s[0]-'0';
        for(int i=1;i<=n;i++)
        {
            if(s[i]>'0'&&i>sad)
            {
                rj+=i-sad;
                sad+=i-sad;
            }
            sad+=s[i]-'0';
        }
        printf("Case #%d: %d\n",br+1,rj);
    }
    return 0;
}
