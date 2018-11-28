#include <iostream>
#include <math.h>
using namespace std;

long long int tobase2(long long int num)
{
    int arr[32]={0},i=0;
    if(num==0)
        return 0;
    while(num!=0)
    {
        arr[i++]=num%2;
        num=num/2;
    }
    i=i-1;
    do
    {
        num=num*10+arr[i];
        i--;
    }while(i!=-1);
    return num;
}

long long int asbase(long long int num , int b)
{
    int i=0;
    long long int sum=0;
    while(num!=0)
    {
        sum = sum + (num%10) * pow(b,i);
        num=num/10;
        i++;
    }
    return sum;
}

long long int isprime(long long int num)
{
    long long int i=2,rt=sqrt(num);
    for(i=2;i<=rt;i++)
        if(num%i==0)
            return i;
    return 1;
}

int main() {
    int cnt=0;
    long long int num=0;
    long long int i=32769,div[12];
    int t,n,j;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
    cin>>n>>j;
    cout<<"Case #"<<i<<":"<<endl;
    long long int p=pow(2,n-1)+1;
    for(int i=p;cnt<j;i=i+2)
    {
        int flg=1;
        num=tobase2(i);
        for(int k=2;k<=10;k++)
        {
            if((div[k]=isprime(asbase(num,k)))==1)
                {
                    flg=0;
                    break;
                }
        }
        if(flg==1)
        {
            cout<<num;
            for(int k=2;k<=10;k++)
            cout<<" "<<div[k];
            cout<<endl;
            cnt++;
        }
    }
    }
	return 0;
}