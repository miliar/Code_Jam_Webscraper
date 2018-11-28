#include<iostream>
using namespace std;
#include<cstdio>
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    long long int num;
    scanf("%d",&t);
    int case1=0;

    while(t--)
    {
        case1++;
        scanf("%lld",&num);
        if(num==0)
            printf("Case #%d: INSOMNIA\n",case1);
        else
        {
        long long int temp=num;
        int product=1;
        long long int actual=num;
        int digits=0;
        while(temp!=0)
        {
            digits++;
            temp=temp/10;
        }
        int flag=0;
        int sleep[10]={0};
        while(flag!=1)
        {
            temp=num;
            //printf("Reachd num:%d\n",temp);
            int no_digits=0;
            int i;
            while(temp!=0)
            {
                no_digits++;
                int rem=temp%10;
                temp=temp/10;
                sleep[rem]=1;
            }
            if(no_digits-digits>=2)
                break;
            int count=0;
            for(i=0;i<10;i++)
            {
                if(sleep[i]==1)
                {
                    count++;
                }
            }
            if(count==10)
                flag=1;
            if(flag!=1)
                product++;
            num=actual*product;
        }

        if(flag==0)
            printf("Case #%d: INSOMNIA\n",case1);
        else
            printf("Case #%d: %lld\n",case1,num);
        }
    }
    return 0;
}
