#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>
using namespace std;
const int maxn=10000;
int num[maxn];
int s(int x)
{
    char ch[maxn];
    sprintf(ch,"%d",x);
    int len=strlen(ch);
    for(int i=0; i<len/2; i++)
    {
        if(ch[i]!=ch[len-1-i])
        {
            return 0;
        }
    }
    return 1;
}
void find()
{
    memset(num,0,sizeof(num));
    num[1]=1;
    for(int i=1; i<2000; i++)
    {
        int m=sqrt(i);
        if(m*m==i)
        {
            if(s(i))
            {
                if(s(m))
                {
                    num[i]=1;
                }
            }
        }
    }
}
int main()
{
    int cas=0;
    freopen("in.txt","r",stdin);
    freopen("a.txt","w",stdout);
    int t;
    find();
    scanf("%d",&t);
    while(t--)
    {
        printf("Case #%d: ",++cas);
        int a,b;
        int cnt=0;
        scanf("%d%d",&a,&b);
        for(int i=a; i<=b; i++)
        {
            if(num[i])
            {
                cnt++;
            }
        }
        printf("%d\n",cnt);
    }
    return 0;
}
