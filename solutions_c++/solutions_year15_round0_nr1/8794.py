#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,i,s,c,d,j;
    string x;
    cin>>t;
    for(j=0;j<t;j++)
    {
        cin>>s;
        cin>>x;
        d=0;
        c=0;
        int a[s+1];
        for(i=0;i<x.length();i++)
            a[i]=x[i]-48;
        for(i=0;i<s;i++)
        {
            c=c+a[i];
            if(c<i+1)
            {
                d=d+i+1-c;
                c=i+1;
            }
        }
        cout<<"Case #"<<j+1<<": "<<d<<endl;
    }
    return 0;
}
