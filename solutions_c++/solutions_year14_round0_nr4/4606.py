#include<stdio.h>
#include<iostream>
#include<queue>
#include<algorithm>
using namespace std;

int n;
double a[1111],b[1111];
int judge1()
{
    if(n==1)return a[0]>b[0]?1:0;
    int count=0;
    int a_min=0,a_max=n-1;
    int b_min=0,b_max=n-1;
    while(a_min<=a_max)
    {
        if(a[a_max]>b[b_max])
        {
            count++;
            a_max--;
            b_max--;
        }
        else if(a[a_min]>b[b_min])
        {
            count++;
            a_min++;
            b_min++;
        }
        else
        {
            a_min++;
            b_max--;
        }
    }
    return count;
}
int judge2()
{
    int pos=0;
    for(int i=0; i<n; i++){
        while(pos<n&&b[pos]<a[i])pos++;
        if(pos==n)return n-i;
        else pos++;
    }
    return 0;
}
int main()
{
    freopen("D-large.in","r",stdin);
    freopen("D.codeout","w",stdout);
    int t;
    cin>>t;
    for(int cnt=1; cnt<=t; cnt++)
    {
        cin>>n;
        for(int i=0; i<n; i++)cin>>a[i];
        for(int i=0; i<n; i++)cin>>b[i];
        sort(a,a+n);
        sort(b,b+n);
//        for(int i=0; i<n; i++)cout<<a[i]<<"\t"<<' ';
//        cout<<endl;
//        for(int i=0; i<n; i++)cout<<b[i]<<"\t"<<' ';
//        cout<<endl;
        printf("Case #%d: %d %d\n",cnt,judge1(),judge2());

    }
}
