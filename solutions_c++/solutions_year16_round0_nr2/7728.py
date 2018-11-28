#include<iostream>
#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define mod 1000000007

int main()
{
    ifstream cin("input2l.in");
    ofstream cout("cj2l.txt");
    int t;
    cin>>t;
    for(int z=1;z<=t;z++)
    {
        string s;
        cin>>s;
        int n=s.size(),flag=0,mflag=0;
        ll co=0;
        for(int i=0;i<n;i++)
        {
            if(s[i]=='-' && flag==0)
            {
                if(mflag==1)
                {
                    continue;
                }
                else
                {
                    mflag=1;
                    co++;
                }
            }
            else if(s[i]=='-' && flag==1 )
            {
                if(mflag==1)
                {
                    continue;
                }
                else
                {
                    mflag=1;
                    co+=2;
                }
            }
            if(s[i]=='+')
            {
                flag=1;
                mflag=0;
            }
        }
        cout<<"Case #"<<z<<": ";
            cout<<co;
            cout<<endl;
    }
    return 0;
}
