using namespace std;
#include<iostream>
#include<stdio.h>
int A[1001];


int main()
{
freopen ("A-large.in","r",stdin);
freopen ("A-large.txt","w",stdout);

long t;
cin>>t;
for(long k=1;k<=t;k++)
{
    int n;
    cin>>n;
    for(int i=0; i<=n; i++)
       scanf("%1d",&A[i]);

    int extra=0; int count=0;

    for(int i=0; i<=n; i++)
    {
        if(A[i]==0)continue;
        if(count<i)
        {  extra+=i-count; count=i;}
        count +=A[i];
    }
    cout <<"Case #"<<k<<": " << extra<<endl;
}
}

