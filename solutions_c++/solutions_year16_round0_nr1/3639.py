#include <iostream>
#include <cstdio>
using namespace std;

int calc(int a[])
{
    int i , flag=1 ;
    for(i=0;i<10;i++)
    {
        if(a[i]==0)
            flag=0;
    }
    return flag ;
}

void doit(int b[] , long long int c)
{
    long long int k ;
    while(c>0)
    {
        k=c%10 ;
        b[k]++;
        c=c/10 ;
    }
}

int main()
{
    int i , t ;
    cin>>t;
    for(i=0;i<t;i++)
    {
        long long int  n , ans , j  ;
        long long int temp ;
        int a[10]={0} , flag=0 ;
        cin>>n;
        if(n==0)
            printf("Case #%d: INSOMNIA\n",i+1);
        else
        {
            for(j=1;;j++)
            {
                temp=j*n ;
                doit(a , temp) ;
                if(calc(a))
                {
                    flag=1;
                    break;
                }
            }
        }
        if(flag==1)
            printf("Case #%d: %lld\n",i+1,temp);
    }
    
    
    return 0;
}