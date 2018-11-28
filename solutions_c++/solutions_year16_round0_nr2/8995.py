#include <iostream>
#include <cstdio>
#include <string>
using namespace std;
long long t,i,j,k,l,p,n,m;
string s;
int main()
{
    freopen("input.txt" , "r" , stdin);
    freopen("output.txt" , "w" , stdout);
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>s;
        k=1;
        for(j=1;j<s.size();j++)
            if(s[j]!=s[j-1])
                k++;
        if(s[s.size()-1]=='+')
            k--;
        cout<<"Case #"<<i<<": "<<k<<endl;
    }
    return 0;
}