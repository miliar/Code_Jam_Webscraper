#include <iostream>
#include<bits/stdc++.h>
using namespace std;
vector<int>v;
bool cheek(int n)
{
    while(n)
    {
        int n1=n%10;
        v[n1]=1;
        n/=10;
    }
    for(int i=0; i<10; i++)
    {

        if(!v[i])return false;
    }
    return true;
}
int main()
{
    freopen("input.txt","r",stdin);//redirects standard input
     freopen("output.txt","w",stdout);//redirects standard output
    int t;
    cin>>t;
    for(int j=0; j<t; j++)
    {
        v.clear();
        v.resize(10);
        int n;
        int i=1;
        cin>>n;
        int n1=n*i;
        if(n==0)printf("Case #%d: INSOMNIA\n",j+1);
       else{ while(!cheek(n1))
        {
            i++;
            n1=n*i;
        }
        printf("Case #%d: %d\n",j+1,n1);
    }
    }
    return 0;
}
