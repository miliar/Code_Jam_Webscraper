#include<iostream>
#include<cmath>
using namespace std;

int isprime(long long n,int base)
{
    long long i=0,num=0,sq;
    int d,flag=0;
    while(n!=0)
    {
        d=n%10;
        num=num+d*pow(base,i++);
        n/=10;
    }
    sq=sqrt(num);
    for(i=2;i<=sq&&flag==0;i++)
    {
        if(num%i==0)
        flag=1;
    }
    return flag;
}

void display(long long n)
{
    long long i=0,j,num=0,c,sq,n1=n;
    int d,flag=0;

    for(j=2;j<11;j++)
    {
        num=0;
        c=0;
        while(n!=0)
        {
            d=n%10;
            num=num+d*pow(j,c++);
            n/=10;
        }
        n=n1;
    sq=sqrt(num);
    flag=0;
    for(i=2;i<=sq&&flag==0;i++)
    {
        if(num%i==0)
        {
            flag=1;
            cout<<" "<<i;
        }
    }
    }
    cout<<endl;
}

int main()
{
    int t,n,j,i,c,flag,car;
    long long num;
    cin>>t;
    while(t--)
    {
        cin>>n>>j;
        c=0;
        flag=1;
        cout<<"Case #1:\n";
        int* arr=new int[n];
        arr[n-1]=1;
        arr[0]=1;
        for(i=1;i<n-1;i++)
        arr[i]=0;
        do
        {
            num=0;
            car=1;
            i=1;
            do
            {
                arr[i]+=car;
                if(arr[i]==2)
                {
                    arr[i++]=0;
                }
                else
                {
                    car=0;
                }
            }
            while(car);
            for(i=n-1;i>=0;i--)
            num=num*10+arr[i];
            c=0;
            flag=1;
            for(i=2;i<=10&&flag==1;i++)
            {
                flag=isprime(num,i);
                c=c+flag;
            }
         //   cout<<" g ";
            if(c==9)
            {
                cout<<num;
                display(num);
                j--;
            }
        }
        while(j);

    }
    return 0;
}
