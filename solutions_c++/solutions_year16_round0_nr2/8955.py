#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int main()
{
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    string s;
    int l;
    for(int k=1;k<=t;k++)
    {
        cin>>s;
        l=s.length();
        long int c=0;
        for(int i=1;i<l;i++)
        {
            if(s[i]!=s[i-1])
                c++;
        }
        if(s[l-1]!='+')
            c++;
        cout<<"Case #"<<k<<": "<<c<<"\n";
    }
    return 0;
}
