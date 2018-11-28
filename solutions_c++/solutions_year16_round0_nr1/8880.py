/*
Rasedur Rahman Roxy
Facebook: www.facebook.com/MdRoxy
E-mail: roxy.xmw@gmail.com
Condeforces: mdroxy

Problem link:
*/

#include<iostream>
#include<fstream>
#include<cstdio>
#include<cstring>
#include<cctype>
#include<cmath>
#include<vector>
#include<map>
#include<algorithm>
#include<set>

#define ll long long
#define read freopen("in.txt","r",stdin)
#define write freopen("out.txt","w",stdout)
#define loop(x,y,z) for(int i=x;i<y;i+=z)
#define cloop(x,y,z) for(int i=x;i>=y;i-=z)
#define PI acos(-1.0)
#define pf printf
#define MAX 100009

using namespace std;

int main()
{
    //read;
    //write;
    ll n,x;
    map<int,bool>mp;
    int tst;
    cin>>tst;
    for(int t=1;t<=tst;t++)
    {
        cin>>n;
        if(n==0)
        {
            pf("Case #%d: INSOMNIA\n",t);
            continue;
        }
        x=n;
        bool f=1;
        int c=1;
        while(f&&c<=101)
        {
            f=0;
            n=x*c;
            while(n)
            {
                mp[n%10]=1;
                n/=10;
            }
            for(int i=0;i<10;i++)
                if(mp[i]==0)
                {
                    f=1;
                    break;
                }
            c++;
        }
        pf("Case #%d: %lld\n",t,x*(c-1));
        mp.clear();
    }
    return 0;
}
