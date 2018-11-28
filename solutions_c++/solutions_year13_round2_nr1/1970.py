#include<cstdio>
#include<algorithm>
#define INF 10000
using namespace std;

int func(int motes[],int n,int a)
{
    int amends[n],total=0;;
    for(int i=0;i<n;i++)
    {
        int counter=0;
        if(a!=1)
        while(motes[i]>=a)
        {
                a+=a-1;
                counter++;
        }
        else
        {
            counter=INF;
        }

        a+=motes[i];
        amends[i]=counter;
        total+=counter;
    }
int    min=n;
    for(int i=0;i<n;i++)
    {
        int bid=total+i;
        if(bid<min)
        min=bid;
        total-=amends[n-1-i];
    }
    return min;
}

int main()
{
    int test;
    scanf("%d",&test);
    for(int x=1;x<=test;x++)
    {
        int a,n;
        scanf("%d %d",&a,&n);
        int motes[n];
        for(int i=0;i<n;i++)
        {
            scanf("%d",&motes[i]);
        }
        sort(motes,motes+n);

        printf("Case #%d: %d\n",x,func(motes,n,a));
    }
}
