#include<iostream>
#include<cstdio>
#include<cmath>
#define LIMIT 10001
using namespace std;

int array[LIMIT];

void generateFairAndSquare();
bool isPelindrome(long long int n);

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("b.txt","w",stdout);
    generateFairAndSquare();
    int t,count;                                          //number of test cases
    cin>>t;
    long long int A,B,a,b;
    for(int i=1;i<=t;i++)
    {
        cin>>A>>B;
        a=ceil(sqrt(A));
        b=floor(sqrt(B));
        count = 0;
        for(int j=a;j<=b;j++)
        {
            if(array[j]==1)
                count++;
        }
        cout<<"Case #"<<i<<": "<<count<<endl;
    }
}

void generateFairAndSquare()
{
    for(int i=0;i<=LIMIT;i++)
    {
        if(isPelindrome(i) && isPelindrome(i*i))
            array[i]=1;
        else
            array[i]=0;
    }
}

bool isPelindrome(long long int n)
{
    long long int temp=n,revNum=0;
    while(temp != 0)
    {
        revNum = revNum*10 + temp%10;
        temp /= 10;
    }
    if(revNum == n)
        return true;
    else
        return false;
}
