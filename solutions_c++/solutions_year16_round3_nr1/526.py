#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<set>
#include<map>
#include<list>
#include<queue>
#include<vector>

#define pii pair<int,int>
#define F first
#define S second
#define MOD 1000000007
#define itt iterator
#define ritt reverse_iterator
#define LL long long

using namespace std;

char itc(int x)
{
    return (char)((int)'A'+x);
}

int t,n,c;
bool ch;
list<int> mlist[1005];

int main()
{
//    freopen("A-large.in","r",stdin);
//    freopen("A-large.out","w",stdout);

    scanf("%d",&t);
    for(int z=1;z<=t;z++)
    {
        scanf("%d",&n);
        for(int i=0;i<n;i++)
        {
            scanf("%d",&c);
            mlist[c].push_back(i);
        }
        printf("Case #%d: ",z);
        for(int i=1000;i>1;i--)
        {
            if(mlist[i].size()==0)  continue;
            else
            {
                for(list<int>::itt it=mlist[i].begin();it!=mlist[i].end();it++)
                {
                    printf("%c",itc(*it));
                    mlist[i-1].push_back(*it);
                    it++;
                    if(it==mlist[i].end())
                    {
                        printf(" ");
                        break;
                    }
                    printf("%c ",itc(*it));
                    mlist[i-1].push_back(*it);
                }
                mlist[i].clear();
            }
        }
        if(mlist[1].size()%2==1)
        {
            printf("%c ",itc(*mlist[1].begin()));
            mlist[1].pop_front();
        }
        for(list<int>::itt it=mlist[1].begin();!mlist[1].empty()&&it!=mlist[1].end();it++)
        {
            printf("%c",itc(*it));
            it++;
            printf("%c ",itc(*it));
        }
        mlist[1].clear();
        printf("\n");
    }
    return 0;
}
