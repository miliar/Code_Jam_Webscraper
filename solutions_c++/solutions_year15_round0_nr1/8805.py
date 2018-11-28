#include<bits/stdc++.h>
using namespace std;
#define read freopen("input.txt","r",stdin)
#define write freopen("output.txt","w",stdout)
int main()
{
    read;
    write;
    long long t,n,ans,c,l,C,tc=0;
    string s;
    cin>>t;
    while(t--)
    {
        cin>>n;
        cin>>s;
        l=s.size();
        c=0,ans=0,C=0;
        //ans=s[0]-48;
        for(int i=0;i<l-1;i++)
        {
            ans=ans+s[i]-48;
            if(ans>=i+1){C=C;}
            else{C++; ans=ans+1;}
        }
        cout<<"Case #"<<++tc<<": "<<C<<endl;
    }
    return 0;
}

