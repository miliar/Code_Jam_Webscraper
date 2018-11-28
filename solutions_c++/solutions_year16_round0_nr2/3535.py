#include <iostream>
#include <string>
using namespace std;

int check(string &s)
{
    int n=s.size(),i;
    for(i=0;i<n;i++)if(s[i]=='-')return 1;
    return 0;
}

void flip(string &s,int l)
{
    int a=0,b=l;
    while(a<=b)
    {
        if(s[a]=='+')s[a]='-';
        else s[a]='+';
        if(a!=b)if(s[b]=='+')s[b]='-';
        else s[b]='+';
        char te=s[a];
        s[a]=s[b];
        s[b]=te;
        a++,b--;
    }
}

int dec(string &s)
{
    int n=s.size(),ss=0;
    while(check(s))
    {
        //cout<<s<<endl;
        int l=n-1;
        while(s[l]=='+')l--;
        if(s[0]=='-')flip(s,l);
        else
        {
            int i,d,a[l+1],ma=-1,mai=-1;
            for(i=0,d=0;i<l+1;i++)
            {
                if(s[i]=='+')d++,a[i]=d;
                else d=0,a[i]=d;
                if(a[i]>ma)ma=a[i],mai=i;
            }
            flip(s,mai);
        }
        ss++;
    }
    return ss;
}

int main()
{
    int tc,tci=0;
    cin>>tc;
    while(tc--)
    {
        tci++;
        string s;
        cin>>s;
        cout<<"Case #"<<tci<<": "<<dec(s)<<endl;
    }
    return 0;
}
