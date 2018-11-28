#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("A-large (5).in","r",stdin);
    freopen("out1.txt","w",stdout);
    int t,z;
    cin>>t;
    for(z=1;z<=t;z++)
    {
        string s;
        cin>>s;
        int c[26]={0},i;
        for(i=0;s[i];i++)
            c[s[i]-'A']++;
    int freq[10]={0};
    freq[0]=c[25];
    c[4]-=c[25];
    c[17]-=c[25];
    c[14]-=c[25];
    c[25]-=c[25];

    freq[2]=c[22];
    c[14]-=c[22];
    c[19]-=c[22];
    c[22]=0;

    freq[4]=c[20];
  //  cout<<freq[4]<<" "<<c[20]<<endl;
    c[5]-=c[20];
    c[14]-=c[20];
    c[17]-=c[20];
    c[20]=0;

    freq[6]=c[23];
    c[18]-=c[23];
    c[8]-=c[23];
    c[23]=0;

    freq[8]=c[6];
    c[4]-=c[6];
    c[8]-=c[6];
    c[7]-=c[6];
    c[19]-=c[6];
    c[6]=0;

    freq[3]=c[19];
    c[7]-=c[19];
    c[17]-=c[19];
    c[4]-=2*c[19];
    c[19]=0;

    freq[5]=c[5];
    c[8]-=c[5];
    c[21]-=c[5];
    c[4]-=c[5];
    c[5]=0;

    freq[7]=c[18];
    c[4]-=2*c[18];
    c[21]-=c[18];
    c[13]-=c[18];
    c[18]=0;

    freq[9]=c[8];
    c[13]-=2*c[8];
    c[4]-=c[8];
    c[8]=0;

    freq[1]=c[14];
    c[13]-=c[14];
    c[4]-=c[14];
    c[14]=0;
    cout<<"Case #"<<z<<": ";
    int j;
    for(i=0;i<10;i++)
    {
        for(j=0;j<freq[i];j++)
            cout<<i;
    }
    cout<<endl;
    }
    return 0;
}
