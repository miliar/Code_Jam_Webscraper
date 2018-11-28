#include<iostream>
#include<cstdio>
#include<cstdlib>
using namespace std;
int main()
{
    int t;
    cin>>t;
    int x=1;
    int fs[5]={1,4,9,121,484};
    while(t--)
    {
        int A,B;
        int ct=0;
        cin>>A>>B;
        for(int i=0;i<5;i++)
        if(fs[i]>=A && fs[i]<=B)
        ct++;
        cout<<"Case #"<<x++<<": "<<ct<<endl;
    }
    return 0;
}
