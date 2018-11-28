#include<iostream>
#include<stdio.h>
#include<bits/stdc++.h>
#include<string.h>
#include<math.h>
using namespace std;

int main()
{   char s[20000];
     int i=0,n,t,cnt=0,k=0;
    cin>>t;
    while(t--)
    {   cnt=0;
        cin>>s;
        n=strlen(s);
    for(i=0;i<n-1;i++)
    {
       if(s[i]!=s[i+1])
        cnt++;
    }
    if(s[n-1]=='-')
        cnt++;
        cout<<"Case #"<<++k<<": "<<cnt<<endl;

   // cout<<cnt;
    }
    return 0;
}
