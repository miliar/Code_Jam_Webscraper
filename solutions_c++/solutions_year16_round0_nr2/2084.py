#include<iostream>
#include<stdio.h>
#include<string>
using namespace std;
int t,n,num;
string s;
int main()
{
    //freopen("a.in","r",stdin);
    //freopen("output.txt","w",stdout);
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {
        cin>>s;
        n=s.size();
        num=0;
        if(s[0]=='-')num++;
        for(int i=1;i<n;i++)
            if((s[i-1]=='+')&&(s[i]=='-'))num=num+2;
        cout<<"Case #"<<tt<<": "<<num<<endl;
    }
    return 0;
}