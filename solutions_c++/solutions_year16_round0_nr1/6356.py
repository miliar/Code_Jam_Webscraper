#include <iostream>

using namespace std;

#include <stdio.h>
#include <stdlib.h>

int main()
{
    freopen ("a.txt","r",stdin);
    freopen ("ao.txt","w",stdout);
    long long test,i;
    scanf("%d",&test);
    for(i=0;i<test;i++)
    {
        long long n,flag=0,k,x,prev=0;
        cin>>n;long long l=1;long long coun[11]={0};
        while(1)
        {

        x=l++*n;
        if(x==prev)
            break;

        //track digits
        k=x;long long d;
        prev=k;
        while(x!=0)
        {
            d=x%10;
            coun[d]=1;
            x=x/10;
        }
        //check digits
        long long check=0;
        for(int j=0;j<=9;j++)
        {
            if(coun[j]>=1)
                check++;
        }
        if(check==10)
            {
                flag=1;break;
            }
        else
            continue;

        }
        printf("Case #%d: ",i+1);
        if(flag==0)cout<<"INSOMNIA";
        else cout<<k;
        printf("\n");flag=0;
    }
    return 0;
}
