#include <iostream>
#include <cstring>
#include <queue>
#include <stdio.h>
#include <cmath>
#include <sstream>
#include <cstdio>
#include <algorithm>
#include <cstdio>
#include <set>
#include <cstdlib>
#include <vector>
#include <cctype>
#include <utility>
#include <map>
#include <string>
using namespace std;

int conversion(string p){ int o; o=atoi(p.c_str()); return o; }
string toString(int h){ stringstream ss; ss<<h; return ss.str(); }
long long gcd(long long a,long long b) {return (b==0 ? a : gcd(b,a%b));}
int lcm(int a,int b) {return (a*(b/gcd(a,b))); }

int main()
{
    ios::sync_with_stdio(1);

    #ifndef ONLINE_JUDGE
    freopen("D:/input.txt","r",stdin);
    //reopen("D:/output.txt","w",stdout);
    #endif

    int T,cas=1;
    cin>>T;
    while(T--)
    {
        int a,b,c,res=0;
        cin>>a>>b>>c;
        for(int i=0;i<a;i++)
        {
            for(int j=0;j<b;j++)
            {
                if((i & j)<c) res++;
            }
        }
        cout<<"Case #"<<cas<<": "<<res<<endl;
        cas++;
    }
}
