#include <bits/stdc++.h>
#define ull unsigned long long

using namespace std;

int main()
{
    ifstream in;
    in.open("A-large.in");
    ofstream out;
    out.open("output.out");

    int t;in>>t;
    for(int i=1;i<t+1;i++)
    {

        out<<"Case #"<<i<<": ";

        string s;
        in>>s;
        ull arr[26]={0},num[10]={0};
        ull ans=0;
        for(ull j=0;j<s.length();j++)
        {
            arr[s[j]-65]++;
        }
        if(arr[25]>0)
        {
            num[0]=arr[25];

                arr['E'-65]-=arr[25];
                arr['R'-65]-=arr[25];
                arr['O'-65]-=arr[25];
            arr[25]=0;
        }
        if(arr['U'-65]>0)
        {
            num[4]=arr['U'-65];

                arr['F'-65]-=arr['U'-65];
                arr['R'-65]-=arr['U'-65];
                arr['O'-65]-=arr['U'-65];
            arr['U'-65]=0;
        }
        if(arr['W'-65]>0)
        {
            num[2]=arr['W'-65];
                arr['T'-65]-=arr['W'-65];
                arr['O'-65]-=arr['W'-65];
                arr['W'-65]=0;
        }
        if(arr['O'-65]>0)
        {
            num[1]=arr['O'-65];

            arr['N'-65]-=arr['O'-65];
            arr['E'-65]-=arr['O'-65];
            arr['O'-65]=0;

        }
        if(arr['G'-65]>0)
        {
            num[8]=arr['G'-65];

            arr['E'-65]-=arr['G'-65];
            arr['I'-65]-=arr['G'-65];
            arr['H'-65]-=arr['G'-65];
            arr['T'-65]-=arr['G'-65];

            arr['G'-65]=0;
        }
        if(arr['X'-65]>0)
        {
            num[6]=arr['X'-65];

            arr['S'-65]-=arr['X'-65];
            arr['I'-65]-=arr['X'-65];

            arr['X'-65]=0;
        }
        if(arr['F'-65]>0)
        {
            num[5]=arr['F'-65];

            arr['V'-65]-=arr['F'-65];
            arr['I'-65]-=arr['F'-65];
            arr['E'-65]-=arr['F'-65];

            arr['F'-65]=0;
        }

        if(arr['R'-65]>0)
        {
            num[3]=arr['R'-65];

            arr['T'-65]-=arr['R'-65];
            arr['H'-65]-=arr['R'-65];
            arr['E'-65]-=2*arr['R'-65];

            arr['R'-65]=0;
        }


        if(arr['V'-65]>0)
        {
            num[7]=arr['V'-65];

            arr['S'-65]-=arr['V'-65];
            arr['N'-65]-=arr['V'-65];
            arr['E'-65]-=2*arr['V'-65];

            arr['V'-65]=0;
        }


        if(arr['I'-65]>0)
        {
            num[9]=arr['I'-65];

            arr['N'-65]-=2*arr['I'-65];
            arr['E'-65]-=arr['I'-65];

            arr['I'-65]=0;
        }


        for(ull j=0;j<10;j++)
        {
            for(ull k=0;k<num[j];k++)
            {
                out<<j;
            }
        }
        out<<"\n";














    }

}
