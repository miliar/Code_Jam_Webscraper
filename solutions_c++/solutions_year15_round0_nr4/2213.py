// Coder nyble
#include <bits/stdc++.h>

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
    cin>>t;
    for(int z=1; z<=t; z++)
    {
        int x,r,c;
        cin>>x>>r>>c;
        bool gab=false;
        if(x==1)
        {
            gab=true;
        }
        else if(x==2)
        {
            if((r*c)%2==0)
                gab=true;
        }
        else if(x==3)
        {
            if((r*c)%3==0&&(r*c)!=3)
                gab=true;
        }
        else if(r*c>=12)
        {
            gab=true;
        }
        if(gab)
            printf("Case #%d: GABRIEL\n",z);
        else
            printf("Case #%d: RICHARD\n",z);
    }
    return 0;
}
