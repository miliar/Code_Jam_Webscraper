#include <iostream>
using namespace std;
#define ll long long

int main()
{   ll x,i;
    cin>>x;
    for(i=0;i<x;++i)
    {   string s;
        cout<<"Case #"<<i+1<<": ";
        cin>>s;
        ll l=0,q=0;
        while(s[l]!='\0')
            ++l;
        for(int j=1;j<l;++j)
            if(s[j]!=s[j-1])
                ++q;
        if(s[l-1]=='+')
            cout<<q<<"\n";
        else
            cout<<q+1<<"\n";
    }
    return 0;
}
