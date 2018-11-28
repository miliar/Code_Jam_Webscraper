#include<stdio.h>
#include<iostream>
using namespace std ;
int main()
{
    long t,max,diff,p,arr[1005],i,sum,test=0;
    char str[1005];
    scanf("%ld",&t);
    while(t--)
    {
        test++;
        scanf("%d%s",&max,&str);
        for(i=0;i<=max;i++)
        arr[i]=str[i]-'0';
        p=arr[0];
        sum=arr[0];
        diff=0;
        for(i=1;i<=max;i++)
        {
            if(sum>=i)
                sum=sum+arr[i];
            else
            {

                diff=diff+(i-sum);
                sum=sum+(i-sum)+arr[i];

            }

        }
        cout<<"Case #"<<test<<": "<<diff<<endl;


    }
}
