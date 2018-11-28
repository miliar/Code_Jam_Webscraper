#include<iostream>
#include<bits/stdc++.h>
#include<cstdio>
using namespace std;

int main()
{
    freopen("inputt.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T,S_max,T_audience,cntr;
    string str;
    cin>>T;
    for(int k=1;k<=T;k++)
    {
        T_audience=0,cntr=0;
        cin>>S_max>>str;
        for(int i=0;i<=S_max;i++)
        {
            if(i!=0)
            {
                if(i>T_audience)
                   {
                     cntr++;T_audience++;//*=i-T_audience;*/cout<<cntr<<"T="<<T_audience<<"i="<<i<<endl;
                   }
                T_audience+=str[i]-48;
            }
            else
                T_audience+=str[i]-48;
        }
        printf("Case #%d: %d\n",k,cntr);
    }
    return 0;
}
