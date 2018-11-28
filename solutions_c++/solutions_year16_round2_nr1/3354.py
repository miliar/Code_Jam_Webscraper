#include<iostream>
#include<stdio.h>
#include<cstring>
using namespace std;

int main()
{
    freopen("a.in","r",stdin);
    freopen("aa.txt","w",stdout);
    int t; cin>>t;

    for(int i=1;i<=t;i++)
    {
        string s; cin>>s;
        int temp,sum=0,len=s.length();

        int cnt[26]={0},digit[10]={0};

        for(int j=0;j<len;j++)
            cnt[s[j]-65]++;

        if(cnt['Z'-'A']>0)
        {
                    temp=cnt['Z'-'A'];
                    digit[0]=temp;
                    cnt['Z'-'A']-=temp;
                    cnt['E'-'A']-=temp;
                    cnt['R'-'A']-=temp;
                    cnt['O'-'A']-=temp;
        }
        if(cnt['W'-'A']>0)
        {
                   temp=cnt['W'-'A'];
                    digit[2]=temp;
                    cnt['T'-'A']-=temp;
                    cnt['W'-'A']-=temp;
                    cnt['O'-'A']-=temp;
        }

        if(cnt['U'-'A']>0)
            {
                    temp=cnt['U'-'A'];
                    digit[4]=temp;
                    cnt['F'-'A']-=temp;
                    cnt['O'-'A']-=temp;
                    cnt['U'-'A']-=temp;
                    cnt['R'-'A']-=temp;
            }
        if(cnt['X'-'A']>0)
            {
                    temp=cnt['X'-'A'];
                    digit[6]=temp;
                    cnt['S'-'A']-=temp;
                    cnt['I'-'A']-=temp;
                    cnt['X'-'A']-=temp;
            }
        if(cnt['G'-'A']>0)
                {
                    temp=cnt['G'-'A'];
                    digit[8]=temp;
                    cnt['E'-'A']-=temp;
                    cnt['I'-'A']-=temp;
                    cnt['G'-'A']-=temp;
                    cnt['H'-'A']-=temp;
                    cnt['T'-'A']-=temp;
                }
        if(cnt['T'-'A']>0)
                {
                    temp=cnt['T'-'A'];
                    digit[3]=temp;
                    cnt['T'-'A']-=temp;
                    cnt['H'-'A']-=temp;
                    cnt['R'-'A']-=temp;
                    cnt['E'-'A']-=temp;
                    cnt['E'-'A']-=temp;
                }
        if(cnt['F'-'A']>0)
                {
                    temp=cnt['F'-'A'];
                    digit[5]=temp;
                    cnt['F'-'A']-=temp;
                    cnt['I'-'A']-=temp;
                    cnt['V'-'A']-=temp;
                    cnt['E'-'A']-=temp;
                }
        if(cnt['V'-'A']>0)
                {
                    temp=cnt['V'-'A'];
                    digit[7]=temp;
                    cnt['S'-'A']-=temp;
                    cnt['E'-'A']-=temp;
                    cnt['V'-'A']-=temp;
                    cnt['E'-'A']-=temp;
                    cnt['N'-'A']-=temp;
                }
        if(cnt['O'-'A']>0)
            {
                temp=cnt['O'-'A'];
                digit[1]=temp;
                cnt['O'-'A']-=temp;
                cnt['N'-'A']-=temp;
                cnt['E'-'A']-=temp;
            }
        if(cnt['N'-'A']>0)
             {
                temp=cnt['N'-'A'];
                temp/=2;
                digit[9]=temp;
                cnt['N'-'A']-=temp;
                cnt['I'-'A']-=temp;
                cnt['N'-'A']-=temp;
                cnt['E'-'A']-=temp;
             }
    cout<<"Case #"<<i<<": ";
    for(int j=0;j<10;j++)
    {
        temp=digit[j];
        while(temp>0)
        {
            cout<<j;
            temp--;
        }
    }
    cout<<endl;
    }
}
