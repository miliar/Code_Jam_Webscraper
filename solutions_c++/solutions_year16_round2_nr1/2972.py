#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<cstring>
using namespace std;
int main()
{
    freopen("A-large (2).in","r",stdin);
    freopen("B1LARGE.txt","w",stdout);
    int t;
    cin>>t;
    for(int q=1;q<=t;q++)
    {
        string s;
        cin>>s;

        int count[26]={0};
        int n=s.length();

        for(int i=0;i<n;i++)
        {

            count[s[i]-65]++;
        }


        int a[1000];int x=0;
        int e;
        if(count[25]>0)
        {
            e=count[25];
            count[25]=0;
            count[4]-=e;
            count[17]-=e;
            count[14]-=e;
            for(int j=0;j<e;j++)
                a[x++]=0;
        }
        if(count[23]>0)
        {
            e=count[23];
            count[23]=0;
            count[19]-=e;
            count[8]-=e;
            for(int j=0;j<e;j++)
                a[x++]=6;
        }
        if(count[6]>0)
        {
            e=count[6];
            count[6]=0;
            count[4]-=e;
            count[8]-=e;
            count[7]-=e;
            count[19]-=e;
            for(int j=0;j<e;j++)
                a[x++]=8;
        }
        if(count[7]>0)
        {
            e=count[7];
            count[7]=0;
            count[19]-=e;
            count[17]-=e;
            count[4]-=e;
            count[4]-=e;
            for(int j=0;j<e;j++)
                a[x++]=3;
        }
        if(count[20]>0)
        {
            e=count[20];
            count[20]=0;
            count[5]-=e;
            count[14]-=e;
            count[17]-=e;

            for(int j=0;j<e;j++)
                a[x++]=4;
        }
        if(count[22]>0)
        {
            e=count[22];
            count[22]=0;
            count[19]-=e;
            count[14]-=e;
            for(int j=0;j<e;j++)
                a[x++]=2;
        }
        if(count[5]>0)
        {
            e=count[5];
            count[5]=0;
            count[8]-=e;
            count[21]-=e;
            count[4]-=e;

            for(int j=0;j<e;j++)
                a[x++]=5;
        }
        if(count[21]>0)
        {
            e=count[21];
            count[21]=0;
            count[18]-=e;
            count[4]-=e;
            count[13]-=e;
            count[4]-=e;
            for(int j=0;j<e;j++)
                a[x++]=7;
        }
        if(count[14]>0)
        {
            e=count[14];
            count[14]=0;
            count[13]-=e;
            count[4]-=e;

            for(int j=0;j<e;j++)
                a[x++]=1;
        }
        if(count[13]>0)
        {
            e=count[13]/2;
            count[13]=0;
            count[4]-=e;
            count[8]-=e;

            for(int j=0;j<e;j++)
                a[x++]=9;
        }
        sort(a,a+x);
        cout<<"Case #"<<q<<": ";
        for(int p=0;p<x;p++)
            cout<<a[p];
        cout<<"\n";
    }
    return 0;
}
