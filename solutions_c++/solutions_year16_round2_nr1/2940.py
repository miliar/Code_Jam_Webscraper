#include <iostream>
#include<stdio.h>
#include<string.h>
using namespace std;

int main()
{
    int t,i,j,k;
    char num[2001];
    int a[26];
    int n[10];
    cin>>t;
    for(i=0;i<t;i++)
    {
        memset(a, 0, 26 * sizeof(a[0]));
        memset(n, 0, 10 * sizeof(n[0]));
        cin>>num;
        for(j=0;j<strlen(num);j++)
        {
            a[num[j]-'A']++;
        }
        if(a[25])
        {
            n[0]=a[25];
            a[25]=0;
            a[4]=a[4]-n[0];
            a[17]=a[17]-n[0];
            a[14]=a[14]-n[0];
        }
        if(a[22])
        {
            n[2]=a[22];
            a[22]=0;
            a[19]=a[19]-n[2];
            a[14]=a[14]-n[2];
        }
        if(a[20])
        {
            n[4]=a[20];
            a[20]=0;
            a[5]-=n[4];
            a[14]-=n[4];
            a[17]-=n[4];
        }
        if(a[23])
        {
            n[6]=a[23];
            a[23]=0;
            a[18]-=n[6];
            a[8]-=n[6];
        }
        if(a[6])
        {
            n[8]=a[6];
            a[6]=0;
            a[4]-=n[8];
            a[8]-=n[8];
            a[7]-=n[8];
            a[19]-=n[8];
        }
        if(a[14])
        {
            n[1]=a[14];
            a[14]=0;
            a[13]-=n[1];
            a[4]-=n[1];
        }
        if(a[19])
        {
            n[3]=a[19];
            a[19]=0;
            a[7]-=n[3];
            a[17]-=n[3];
            a[4]=a[4]-n[3]-n[3];
        }
        if(a[5])
        {
            n[5]=a[5];
            a[5]=0;
            a[8]-=n[5];
            a[21]-=n[5];
            a[4]-=n[5];
        }
        if(a[18])
        {
            n[7]=a[18];
            a[18]=0;
            a[21]-=n[7];
            a[13]-=n[7];
            a[4]=a[4]-n[7]-n[7];
        }
        if(a[13])
        {
            n[9]=a[13]/2;
            a[13]=0;
        }
        cout<<"Case #"<<i+1<<": ";
        for(j=0;j<10;j++)
        {
            //cout<<j<<" "<<n[j]<<endl;
            for(k=0;k<n[j];k++)
                cout<<j;
        }
        cout<<endl;
    }
    return 0;
}
