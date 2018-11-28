#include <iostream>
#include<bits/stdc++.h>
using namespace std;
bool checkarray(int count[])
{
    int i;
    for(i=0;i<=9;i++)
    {
        if(count[i]==0)
            return false;
    }
    return true;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("code.o","w",stdout);
    int t,n,i;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>n;
        if(n==0)
        {
            cout<<"Case #"<<i<<": INSOMNIA"<<endl;
            continue;
        }
        int count[10]={0};
        int n1;
        int j=0;
        while(checkarray(count)!=true)
        {
            j++;
            n1=n*j;
            while(n1!=0)
            {
                count[n1%10]++;
                n1=n1/10;
            }
            n1=n*j;
        }
        cout<<"Case #"<<i<<": "<<n1<<endl;
    }
    return 0;
}
