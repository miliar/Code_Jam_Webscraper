#include <bits/stdc++.h>

typedef long long int ll;
typedef unsigned long long int ull;
typedef long double ld;

#define mp make_pair
#define pb push_back
#define bp __builtin_popcount

#define mt(a,b,c) mp(a,mp(b,c))
#define min3(a,b,c) min(a,min(b,c))

const ll mo=1e9+7;
const ll INF=1e17;
const ld pi=acos(-1);
const int mxn=2e5+5;
const int cons=1;

using namespace std;

int main()
{
    freopen("in.in","r",stdin);
    freopen("output.txt","w",stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T,t,k,i,j,ct;
    bool f;
    string s;
    cin>>T;
    for(t=1;t<=T;t++)
    {
        cout<<"Case #"<<t<<": ";
        cin>>s>>k;
        ct=0;
        for(i=0;i<=(int)s.length()-k;i++)
        {
            if(s[i]=='-')
            {
                ct++;
                for(j=0;j<k;j++)
                {
                    if(s[i+j]=='+')
                    {
                        s[i+j]='-';
                    }
                    else
                    {
                        s[i+j]='+';
                    }
                }
            }
        }
        f=1;
        for(i=0;i<(int)s.length();i++)
        {
            if(s[i]=='-')
            {
                f=0;
            }
        }
        if(f)
        {
            cout<<ct<<"\n";
        }
        else
        {
            cout<<"IMPOSSIBLE\n";
        }
    }
    return 0;
}
