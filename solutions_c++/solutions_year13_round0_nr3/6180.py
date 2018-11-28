#include<iostream>
#include<string>
#include<stdio.h>
using namespace std;
int main()
{
    int f,l,t,c=0;
    cin>>t;
    for(int i=0;i<t;i++)
    {
    cin>>f;
    cin>>l;
    c=0;

    if(1>=f && 1<=l)
        c+=1;
    if(4>=f && 4<=l)
        c+=1;
        if(9>=f && 9<=l)
        c+=1;
     if(121>=f && 121<=l)
        c=c+1;
     if(484>=f && 484<=l)
        c+=1;
     cout<<"Case #"<<i+1<<": "<<c<<endl;
    }

}
