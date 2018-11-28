#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
using namespace std;
int s[2000];

bool judge(int num)
{
    int tmp[100];
    int pos=0;
    while (num)
    {
        tmp[pos++]=num%10;
        num/=10;
    }
    for (int i=0; i<(pos)/2; i++)
        if (tmp[i]!=tmp[pos-i-1]) return false;
    return true;
}
int init()
{
    memset(s,0,sizeof(s));
    for (int i=1; i<=1000; ++i)
        if (judge(i) && judge (i*i))
        {
            s[i]=s[i-1]+1;
            //cout<<".............."<<i<<endl;
        }
        else s[i]=s[i-1];
}

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C.out","w",stdout);
    int cas,Cas,a,b;
    init();
    scanf("%d",&Cas);
    for (int cas=1;cas<=Cas;cas++)
    {
        scanf("%d %d",&a,&b);
        int aa,bb;
        aa=sqrt(a);
        bb=sqrt(b);
        if (aa*aa==a) aa--;
        printf("Case #%d: %d\n",cas,s[bb]-s[aa]);
    }
    return 0;
}
