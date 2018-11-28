#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<vector>
using namespace std;

int sum_of_array(int a[10])
{
    long long sum =0;
    for (int i=0; i<10; i++)
    {
        sum+=a[i];
    }
    if (sum==(-1))
    {
        return 1;
    }
    else
        return 0;
}
int divide(long long n,int a[10])
{
    long long r,x;
    long s;
    while (n!=0)
    {
        r=n%10;
        n=n/10;
        if (r==0)
        {
            a[0]=(-1);
            s=sum_of_array(a);
            if (s==1)
            {
                return 1;
            }
        }
        else if (r==1)
        {
            a[1]=0;
            s=sum_of_array(a);
            if (s==1)
            {
                return 1;
            }
        }
        else if (r==2)
        {
            a[2]=0;
            s=sum_of_array(a);
            if (s==1)
            {
                return 1;
            }
        }
        else if (r==3)
        {
            a[3]=0;
            s=sum_of_array(a);
            if (s==1)
            {
                return 1;
            }
        }
        else if (r==4)
        {
            a[4]=0;
            s=sum_of_array(a);
            if (s==1)
            {
                return 1;
            }
        }
        else if (r==5)
        {
            a[5]=0;
            s=sum_of_array(a);
            if (s==1)
            {
                return 1;
            }
        }
        else if (r==6)
        {
            a[6]=0;
            s=sum_of_array(a);
            if (s==1)
            {
                return 1;
            }
        }
        else if (r==7)
        {
            a[7]=0;
            s=sum_of_array(a);
            if (s==1)
            {
                return 1;
            }
        }
        else if (r==8)
        {
            a[8]=0;
            s=sum_of_array(a);
            if (s==1)
            {
                return 1;
            }
        }
        else if (r==9)
        {
            a[9]=0;
            s=sum_of_array(a);
            if (s==1)
            {
                return 1;
            }
        }
    }

    return 0;

}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out1.txt","w",stdout);
    long long t;
    cin>>t;
    for (int i=1; i<=t; i++)
    {
        long long n,n1;
        cin>>n;

        n1=n;
        if (n==0)
        {
            cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
        }
        else
        {
            int a[10] = {1,1,1,1,1,1,1,1,1,1};
            int a1;
            for (int j=1; ; j++)
            {
                long long s;
                s=n*j;
                a1=divide(s,a);
                if (a1==1)
                {
                    cout<<"Case #"<<i<<": "<<s<<endl;
                    break;
                }

            }
        }


    }
}
