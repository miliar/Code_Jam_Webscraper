#include<cstdio>
#include<iostream>
#include<conio.h>
#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin>>t;
    for( int h=1;h<=t;h++)
    {
        string st;
       cin>>st;
       int i=1;
       char ch=st[0];
       int counts=0;
       while(st[i]!='\0')
       {
           if(st[i]!=ch)
           {
               counts++;
               ch=st[i];
           }
           i++;
       }
       if(st[i-1]=='-')
        cout<<"Case #"<<h<<": "<<counts+1<<"\n";
       else
        cout<<"Case #"<<h<<": "<<counts<<"\n";



}
}
