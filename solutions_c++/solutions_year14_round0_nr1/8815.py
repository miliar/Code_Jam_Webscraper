#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <utility>
#include <vector>
#define mp make_pair
#define xx first
#define yy second
#define pb push_back
using namespace std;
vector<int> ve,f,n;
int t,a,k,c;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
	scanf("%d",&t);
	int CASE=0;
	while (t--)
    {
        scanf("%d",&a);
        ve.clear();
        f.clear();
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                scanf("%d",&k);
                if(i==a-1)ve.pb(k);
            }
        }

        scanf("%d",&a);
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                scanf("%d",&k);
                if(i==a-1)f.pb(k);
            }
        }
        n.clear();
        n.resize(4,-1);
        sort(f.begin(),f.end());
        sort(ve.begin(),ve.end());
        set_intersection(f.begin(),f.end(),ve.begin(),ve.end(),n.begin());
        c=4;
        for(int i=0;i<4;i++)if(n[i]==-1){c=i;break;}
        printf("Case #%d: ",++CASE);
        if(c>1)printf("Bad magician!\n");
        if(c==0)printf("Volunteer cheated!\n");
        if(c==1)printf("%d\n",n[0]);
    }
    return 0;
}
