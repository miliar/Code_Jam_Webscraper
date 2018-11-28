#include<bits/stdc++.h>
using namespace std;
int flag[10]={0};
void csheep(long long n)
{

    while(n>9)
    {
        flag[(n%10)]=1;
        n=n/10;
    }

    flag[(n%10)]=1;
}
int check(int i)
{
    /*if(flag[i]==0)
        return 0;
    if(i==10)
        return 1;
    return(check(i+1));*/
    for(i=0;i<10;i++)
        if(flag[i]==0)
            return 0;
    return 1;

}
int main()
{
    int t,x=0;
    scanf("%d",&t);
    while(t--)
    {
        int i=1,flag1=0;
        long long n;
        ++x;
        memset(flag,0,sizeof flag);
        scanf("%lld",&n);
        while(1)
        {
            if(n*i==0)
                break;
            csheep(n*i);
            if(check(0)==1)
            {
                break;
            }

            i++;
        }
        printf("Case #%d: ",x);
        if(n*i==0)
            printf("INSOMNIA\n");
        else
            printf("%lld\n",n*i);





    }
    return 0;
}
