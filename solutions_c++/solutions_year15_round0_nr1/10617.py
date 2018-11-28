#include<iostream>

using namespace std;

int main()
{
    int t,s,count,i,j;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>s;
        char aud[s+1];
        cin>>aud;
        count = 0;
        for(j=0;j<=s;j++)
        {
            if(aud[j]-'0'>1&&j<s)
            {
                aud[j+1]=((aud[j+1]-'0')+(aud[j]-'0')-1)+'0';
                aud[j]='1';
            }
        }
        for(j=0;j<=s;j++)
        {
            if(aud[j]=='0')
                count++;
        }
        cout<<"Case #"<<i<<":"<<" "<<count<<endl;
    }

    return 0;
}
