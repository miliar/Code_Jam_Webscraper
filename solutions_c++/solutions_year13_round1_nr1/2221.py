#include<iostream>
#include<cstdio>
using namespace std;
int r,t;
int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    int test=1;
    while(T--)
    {
        scanf("%d%d",&r,&t);
        int num=0;
        while(t>=0)
        {
           t-=(2*r+1);
           r=r+2;
           num++;
        }
        printf("Case #%d: %d\n",test++,num-1);
    }
    return 0;
}
