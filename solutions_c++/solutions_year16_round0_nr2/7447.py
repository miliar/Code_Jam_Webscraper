#include<bits/stdc++.h>
#include <iostream>
using namespace std;
#define ll long long
string reverse(string s , int size)
{
    for(int i = 0 ; i <= size ; i++)
    {
        char temp = s[i];
        s[i] = s[size - i];
        s[size - i] = temp;
    }
    return s;
}
bool allplus(string s)
{
    ll len=s.length();ll flag=0;
    for(ll i =0;i<len;i++)
    {
        if(s[i]=='+')
        flag=1;
        else
        {
        flag=0;
        break;
        }
    }
    if(flag==1)
    return true;
    else
    return false;
}

bool allminus(string s)
{
    ll len=s.length();ll flag=0;
    for(ll i =0;i<len;i++)
    {
        if(s[i]=='-')
        flag=1;
        else
        {
        flag=0;
        break;
        }
    }
    if(flag==1)
    return true;
    else
    return false;
}
int main()
{
   // cout << "Hello World!" << endl;
    ll tc;
    cin>>tc;
    for(ll i=1;i<=tc;i++)
    {
        string s; int flag=0;
        cin>>s;
        ll len=s.length();
        ll c=0;
        if(len==1 and s=="+"){
        cout<<"Case #"<<i<<": 0"<<endl;continue;}
        
        else if(len==1 and s=="-"){
        cout<<"Case #"<<i<<": 1"<<endl;continue;}
        
        else if(allplus(s)){
        cout<<"Case #"<<i<<": 0"<<endl;continue;}
        
        else if(allminus(s)){
        cout<<"Case #"<<i<<": 1"<<endl;continue;}
        
        while(flag!=111)
        {
         for(ll k=0;k<len-1;k++)
         {
             if((s[k]=='-' and s[k+1]=='+') || (s[k]=='+' and s[k+1]=='-'))
             {//flip(0,k);
             flag=0;
             reverse(s , k);
                 for(ll a=0;a<=k;a++)
                 {
                     if(s[a]=='+')
                     s[a]='-';
                     else
                     s[a]='+';
                 }
                 c++;
             }
             else if(allplus(s))
             {flag=111;
              break;
             }
              else if(allminus(s))
              {
                  flag=111;
                  c=c+1;
                  break;
              }
             
         }
        }
        cout<<"Case #"<<i<<": "<<c<<endl;
    }
    return 0;
}

