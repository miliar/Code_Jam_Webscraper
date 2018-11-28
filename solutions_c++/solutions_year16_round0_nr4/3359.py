#include <bits/stdc++.h>
using namespace std;
long long int power(long long int b,long long int p)
{
    if(p==0)
    {
        return 1;
    }
    else
    {
        long long int val=power(b,p/2);
        if(p%2==0)
        {
            return val*val;
        }
        else
        {
            return val*val*b;
        }
    }
}

int main()
{
    long long int t,t1=1,k,c,s,val,add,i;
    cin>>t;
    while(t1<=t)
    {
        cin>>k>>c>>s;
        cout<<"Case #"<<t1<<": ";
        val=1;
        add=power(k,c-1);
        for(i=0;i<s;i++)
        {
            cout<<val<<" ";
            val+=add;
        }
        cout<<endl;
        t1++;
    }
    return 0;
}
