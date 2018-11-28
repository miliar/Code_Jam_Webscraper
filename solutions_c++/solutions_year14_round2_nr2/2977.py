#include<iostream>
#include<algorithm>
#include<vector>
#include<cstdio>
#include<cmath>

using namespace std;

#define rep(i,n) for(int i=0;i<n;i++)
#define s(N) scanf("%d",&N)
#define pb push_back
#define all(x) x.begin(),x.end()

int main()
{
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    int T, counte=0;
    long a, b, c, ans;
    double a1, b1, c1;
    s(T);
    while(T>0)
    {
        T--;
        ans=0;
        s(a);
        s(b);
        s(c);
        for(int i=0;i<a;i++)
        {
            for(int j=0;j<b;j++)
            {
                if((i&j)<c)
                    ans++;
            }
        }
        cout<<"Case #"<<++counte<<": "<<ans<<endl;
    }
    return 0;
}
