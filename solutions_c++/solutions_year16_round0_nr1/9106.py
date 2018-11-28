#include <iostream>
#include <bits/stdc++.h>

using namespace std;



string to_string(int n)
{
    ostringstream temp;
        temp << n;
        return temp.str();
}

int solve (int m)
{
    int c,inc=1,n;
    set <int> myset;
    string s;

    while (true)
    {
        if(myset.size()==10)
            break;

        n=m*(inc++);
        s=to_string(n);

        for(int i=0; i<s.length(); i++)
        {
            myset.insert(s[i]-'0');
        }
    }
    return n;
}


int main()
{
    freopen("A-large.in","r",stdin);
    freopen("solution.out","w",stdout);


    int t,n,p;
    cin>>t;
    p=t;
    for(int i=1; i<=t; i++)
    {
        cin>>n;
        if(n==0)
            cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
        else
            cout<<"Case #"<<i<<": "<<solve(n)<<endl;
    }
    return 0;
}
