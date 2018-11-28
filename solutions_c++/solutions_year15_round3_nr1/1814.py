// Coder nyble
#include <bits/stdc++.h>
#include <cstdio>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
typedef vector<string> vs;

#define fi          first
#define se          second
#define all(x)      (x).begin(), (x).end()
#define ini(a, v)   memset(a, v, sizeof(a))
#define re(i,s,n)  	for(int i=s;i<(n);++i)
#define fr(i,n)     re(i,0,n)
#define tr(i,x)     for(__typeof(x.begin()) i=x.begin();i!=x.end();++i)
#define pu          push_back
#define mp          make_pair
#define sz(x)       (int)(x.size())
#define nl          printf("\n")

int main()
{
    int t;
    scanf("%d",&t);
    for(int z=1;z<=t;z++)
    {
        int r,c,w;
        cin>>r>>c>>w;
        int ans=0;
        if(w==1)
        {
            ans = r*c;
        }
        else if(r==1 && w==c)
        {
            ans = r*c;
        }
        else
        {
            if(c%w==0)
            {
                ans = (((c/w)-1)+w);
            }
            else
            {
                ans= (c/w)+w;
            }
        }

        if(1)
        {
            printf("Case #%d: ",z);cout<<ans<<endl;
        }
    }
    return 0;
}
