#include<bits/stdc++.h>
using namespace std;
#define ll long long
ll i,j,k,l,m,n;
string str;
void flip(ll f)
{
    ll k;string temp=str;
    for(k=0;k<=f;k++)
    {
         str[k]=temp[f-k];
        if(str[k]=='+')
        {
            str[k]='-';
        }
        else
        {
            str[k]='+';
        }
    }
}
int main()
{
    ll t;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cout<<"Case #"<<i<<":"<<" ";
        cin>>str;ll cou=0;
        sree:
        for(j=0;j<str.size();j++)
        {
            if(str[j]=='-'&&str[j-1]=='+')
            {
                flip(j-1);
                cou++;
                goto sree;
            }
            else if(str[j]=='+'&&str[j-1]=='-')
            {
                flip(j-1);
                cou++;
                goto sree;
            }
            
        }
        if(str[0]=='+')
            cout<<cou<<endl;
        else
            cout<<cou+1<<endl;
        //cout<<str<<endl;
    }
}
