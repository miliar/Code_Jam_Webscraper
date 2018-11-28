#include<bits/stdc++.h>
using namespace std;
int main(void)
{
    long long int t,n,a[10];
    //ifstream cin("B-large.in");
    //ofstream cout("output.txt");
    cin>>t;
    string s;
    for(int i=0;i<t;i++)
    {
        cin>>s;
        int ans=0,l=(s.length()-1);
        if(s[s.length()-1]=='+')
        {
            ans=-2;
            for(int j=(s.length()-1);j>=0;j--)
            {
                if(s[j]=='-')
                {
                    s=s.substr(0,j+1);
                    ans=0;
                    break;
                }
            }
        }
        if(s[0]=='-')
        {
            int temp=0;
            for(int j=0;j<s.length()-1;j++)
            {
                if(s[j]!=s[j+1])
                {
                    temp++;
                }
            }
            ans=(temp+1);
        }
        else
        {
            ans++;
            for(int j=0;j<s.length();j++)
            {
                if(s[j]=='+')
                {
                    s[j]='-';
                }
                else
                {
                    break;
                }
            }
            int temp=0;
            for(int j=0;j<s.length()-1;j++)
            {
                if(s[j]!=s[j+1])
                {
                    temp++;
                }
            }
            ans=(ans+temp+1);
        }
        cout<<"Case #"<<(i+1)<<": "<<ans<<endl;
    }
    return 0;
}

