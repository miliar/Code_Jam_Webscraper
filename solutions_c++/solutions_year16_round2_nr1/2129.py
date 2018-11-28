#include<iostream>
#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int times;
    cin>>times;
    int times_copy=times;
    cin.ignore();

    int a[26];
    int count[10];
    int i, j;

    while(times--)
    {
        for(i=0;i<26;i++) a[i]=0;
        for(i=0;i<10;i++) count[i]=0;

        string s;
        getline(cin, s);
        for(i=0;i<s.length();i++)
            a[s[i]-'A']++;
        count[0]=a['Z'-'A'];
        count[2]=a['W'-'A'];
        count[4]=a['U'-'A'];
        count[6]=a['X'-'A'];
        count[8]=a['G'-'A'];
        count[3]=a['H'-'A']-count[8];
        count[7]=a['S'-'A']-count[6];
        count[5]=a['V'-'A']-count[7];
        count[9]=a['I'-'A']-count[8]-count[6]-count[5];
        count[1]=a['O'-'A']-count[4]-count[2]-count[0];

        cout<<"Case #"<<times_copy-times<<": ";
        for(i=0;i<10;i++)
            for(j=0;j<count[i];j++) cout<<i;
        cout<<endl;



    }
    return 0;
}
