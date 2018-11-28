#include<iostream>
#include<stdio.h>
#include<cmath>
#include <bitset>
#include<string>

using namespace std ;

int main()
{
    int T;
    string S,S1;
    freopen("A-large.in","r",stdin) ;
    freopen("aout.txt","w",stdout) ;
    cin>>T;
    for (int j=1;j<=T;j++)
    {
        cin>>S;
        int n=S.length();
        S1=S[0];
        for (int i=1;i<n;i++)
        {
            if (S[i]>=S1[0])
                S1=S[i]+S1;
            else
                S1=S1+S[i];
        }
        cout<<"Case #"<<j<<": "<<S1<<endl;
    }
}
