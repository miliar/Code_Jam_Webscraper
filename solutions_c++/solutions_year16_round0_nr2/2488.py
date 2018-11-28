#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<set>
#include<map>
#include<cmath>
#include<queue>
#include<vector>
#define eps 1e-9
#define mod 1000000007
using namespace std;
int t;
long long n;
string s,s0;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("a.out","w",stdout);
    cin>>t;
    for(int __=1;__<=t;++__)
    {
        cin>>s;

         cout<<"Case #"<<__<<": ";
         s="*"+s;
         s0="";
         for(int i=1;i<(int)s.length();++i)
            if(s[i]!=s[i-1])
                s0+=s[i];
         if(s0[(int)s0.length()-1]=='+')s0=s0.substr(0,(int)s0.length()-1);
         cout<<(int)s0.length()<<endl;
    }

    return 0;
}

// 001011 -4
// 010101 -6
