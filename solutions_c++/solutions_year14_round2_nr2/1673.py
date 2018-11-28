#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <algorithm>
#define ll long long
using namespace std;

map<int,int>m;
bool bi[1002];

int main()
{
    freopen("0.in","r",stdin);
    freopen("0.out","w",stdout);

    int a,b,c,d,e,x,y,z,n;

    int t;

    cin>>t;

    for(int i=1;i<=t;i++)
    {
        printf("Case #%d: ",i);

        int A,B,K;

        cin>>A>>B>>K;
        m.clear();

        for(a=0;a<A;a++)
        {
            for(b=0;b<B;b++) m[ (a&b) ]++;
        }

        for(a=0;a<=1000;a++) bi[a]=false;

        int ans=0;

        for(a=0;a<K;a++)
        {
            for(b=0;b<K;b++)
            {
                c=(a&b);
                if(!bi[c])
                {
                    ans=ans+m[c];
                    bi[c]=true;
                }
            }
        }
        cout<<ans<<endl;
    }

    return 0;
}
