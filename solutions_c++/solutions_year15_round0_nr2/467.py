#include<cstdio>
#include<cmath>
#include<set>
#include<algorithm>
#define pii std::pair<int,int>

using namespace std;

struct compare
{
    bool operator ()(pii x,pii y)
    {
        return (double)x.first/x.second>(double)y.first/y.second;
    }
};

multiset<pii,compare> mset;
int t,n,x,mn,c,ch;
pii g;

int main()
{
//    freopen("B-large.in","r",stdin);
//    freopen("B_out_large.txt","w",stdout);
    scanf("%d",&t);
    for(int z=1;z<=t;z++)
    {
        mn=-2e9;
        c=0;
        scanf("%d",&n);
        for(int i=0;i<n;i++)
        {
            scanf("%d",&x);
            mset.insert(pii(x,1));
            mn=max(x,mn);
        }
        for(int i=0;i<1000;i++)
        {
            c++;
            g=*(mset.begin());
            g.second++;
            mset.erase(mset.begin());
            mset.insert(g);
            ch=c+(int)ceil((double)(*(mset.begin())).first/(*(mset.begin())).second);
            mn=min(mn,ch);
        }
        mset.clear();
        printf("Case #%d: %d\n",z,mn);
    }
    return 0;
}
