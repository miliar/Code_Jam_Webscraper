#include<iostream>
#include<cstdio>
#include<algorithm>
#include<string>
#include<cmath>
using namespace std;
int q[1001]={0};
int palin(int x)
{
    int i=0,j,f=0,ar[1001];
    while(x>0)
    {
        ar[i]=x%10;
        x=x/10;
        i++;
    }
    for(int j=0;j<i;j++)
    {
        if(ar[j]!=ar[i-j-1])
        {
            f=1;break;
        }
    }
    if(f==1) return 0;
    else return 1;
}
int main()
{
    int t;
    scanf("%d",&t);
    int e;
    for(int i=1;i*i<=1000;i++)
    {
        if(palin(i)==1)
        {
            e=i*i;
            if(palin(e)==1) q[e]=1;
        }
    }
    int k=1;
    while(t--)
    {
        int a,b;
        cin>>a>>b;
        int c=0;
        for(int i=a;i<=b;i++)
        {
            if(q[i]==1) c++;
        }
        cout<<"Case #"<<k<<": "<<c<<endl;k++;
    }
    return 0;
}
