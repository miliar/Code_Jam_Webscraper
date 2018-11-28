#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef map<int,int> mii;
typedef vector<int> vi;
typedef vector< vector<int> > vvi;
typedef vector<char> vc;
typedef vector<bool> vb;
typedef vector<string> vs;

#define rep(i,n) for(int i=0;i<n;i++)
#define forup(i,a,b) for(int i=a;i<=b;i++)
#define fordn(i,a,b) for(int i=a;i>=b;i--)
#define all(x) x.begin(),x.end()
#define permute(x) next_permutation(all(x))
#define pb push_back

#define debug if(printf("GD "))
#define mod 1000000007

int main()
{
    int t, d, p[1005], cases = 1;
    int mark[1005];
    scanf("%d",&t);
    while(t--)
    {
        memset(mark,0,sizeof(mark));
        scanf("%d",&d);
        vi v;
        rep(i,d)
        {
            scanf("%d",&p[i]);
            if(mark[p[i]]==0)
                v.pb(p[i]);
            mark[p[i]]++;
        }
        sort(all(v));
        int last = v.size()-1;
        int best = v[last];
        for(int x=1; x<v[last]; x++)
        {
            int temp = x;
            for(int i=last; x<v[i] && i>-1; i--)
            {
                //debug cout<<"Here "<<temp<<" "<<i<<" "<<v[i]<<endl;
                temp = temp + mark[v[i]]*(ceil(v[i]/float(x))-1);
            }
            //debug cout<<x<<" "<<temp<<" "<<best<<endl;
            best = min(temp,best);
        }
        printf("Case #%d: %d\n",cases++,best);
    }
    return 0;
}
