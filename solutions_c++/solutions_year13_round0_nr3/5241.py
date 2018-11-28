#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
    int t;int cases,i,a,b;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    for(cases = 1; cases <= t;cases++)
    {
        scanf("%d%d",&a,&b);
        int num = 0;
        for(i = a; i <= b;i++)
        {
            if(i == 1 || i == 4 || i == 9 || i ==121 ||i ==484)
                num++;
        }
        printf("Case #%d: %d\n",cases,num);
    }
}
