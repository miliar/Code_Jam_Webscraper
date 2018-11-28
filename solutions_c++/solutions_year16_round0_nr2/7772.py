#include<iostream>
#include<cstdio>
#include<string>
using namespace std;

string flip(string str, int n)
{
    for(int i=0;i<=n;i++)
    {
        if(str[i] == '+') str[i]='-';
        else str[i]='+';
    }
    return str;
}

int main()
{
    int t,l;
    long a;
    string vd;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        cin>>vd;
        l=vd.length();
        a=0;
        for(int j=l-1;j>=0;j--)
        {
            if(vd[j]=='-') { vd=flip(vd,j); a++;}
        }
        cout<<"Case #"<<i<<": "<<a<<"\n";
    }
    return 0;
}
