#include<stdio.h>
#include<iostream>
#define MAX 1000001
using namespace std;

int a[MAX];

long long int reverse(long long int n)
{
    long long int num=0;
    while(n!=0)
    {
        num = num*10 + n%10;
        n = n/10;
    }
    return num;
}

void prepareArray()
{
    a[1]=1;
    long long int reverseNum;
    for(long long int i=2;i<MAX;i++)
    {
        if(i%10==0)
        {
            a[i] = a[i-1] + 1;
            continue;
        }
        reverseNum = reverse(i);
        if(reverseNum < i)
        {
            if((a[i-1] + 1) < (a[reverseNum] + 1))
            {
                a[i] = a[i-1] + 1;
            }
            else
            {
                a[i] = a[reverseNum] + 1;
            }
        }
        else
        {
            a[i] = a[i-1] + 1;
        }
    }
}

int main()
{
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    prepareArray();
    int t;
    long long int N;
    cin>>t;
    for(int caseNo=1;caseNo<=t;caseNo++)
    {
        cin>>N;
        cout<<"Case #"<<caseNo<<": "<<a[N]<<endl;
    }
}
