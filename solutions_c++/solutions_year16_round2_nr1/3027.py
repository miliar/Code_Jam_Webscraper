#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t;cin>>t;
    for(int z=1;z<=t;++z)
    {
        string s;cin>>s;
        int i,j,n=s.length(),f=0,x[10]={0},y[26]={0};
        printf("Case #%d: ",z);
        for(i=0;i<n;++i)
        y[s[i]-'A']++;
        for(i=0;i<n;++i)
        {
            if(s[i]=='Z'){x[0]++;y[4]--;y['R'-'A']--;y['O'-'A']--;}
            if(s[i]=='W'){x[2]++;y['T'-'A']--;y['O'-'A']--;}
            if(s[i]=='U'){x[4]++;y[5]--;y['O'-'A']--;y['R'-'A']--;}
            if(s[i]=='X'){x[6]++;y['S'-'A']--;y['I'-'A']--;}
            if(s[i]=='G'){y[4]--;y[8]--;x[8]++;y[7]--;y['T'-'A']--;}
        }
        x[1]=y['O'-'A'];
        x[3]=y['H'-'A'];
        x[5]=y['F'-'A'];
        x[7]=y['V'-'A']-x[5];
        x[9]=y['I'-'A']-x[5];
        for(i=0;i<10;++i)
        {
            for(j=0;j<x[i];++j)
            printf("%d",i);
        }
        printf("\n");
    }
    return 0;
}
