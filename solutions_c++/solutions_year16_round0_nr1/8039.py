#include <iostream>
#include <stdio.h>
#include <vector>
using namespace std;
vector<int> d(10);

void clear()
{
    for(int i=0;i<10;i++) d[i]=0;
    return;
}

bool check()
{
    for(int i=0;i<10;i++) if(d[i]==0) return false;
    return true;
}

void digit(int t)
{
    int p=t;
    while(p)
    {
        d[p%10]++;
        p/=10;
    }
    return;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.out","w",stdout);
    int q;
    scanf("%d",&q);
    for(int i=0;i<q;i++)
    {
        clear();
        int n,t,k=2;
        scanf("%d",&n);
        if(n==0) {printf("Case #%d: INSOMNIA\n",i+1);continue;}
        t=n;
        digit(t);
        while(!check())
        {
            t=k*n;
            k++;
            digit(t);
        }
        printf("Case #%d: %d\n",i+1,t);
    }
    return 0;
}