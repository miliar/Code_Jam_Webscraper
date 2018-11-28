#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<vector>
using namespace std;
#define gc getchar_unlocked()

int main()
{
int i,j,a,b,k,t,num=1;
long count=0;
cin>>t;
while(t--)
{
cin>>a>>b>>k;
for(j=0;j<a;j++)
{for(i=0;i<b;i++)
    {if((j&i)<k)
        count++;
    }
}
cout<<"Case #"<<num<<": "<<count<<"\n";
count=0;num++;
}
    return 0;
}