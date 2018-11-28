#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <queue>
#include <vector>

using namespace std;

int p1,p2,x;
int ca=0;
vector<int> v;

void work()
{
    v.clear();
    scanf("%d",&p1);
    for (int i=1;i<=4;++i)
        for (int j=1;j<=4;++j)
            {
                scanf("%d",&x);
                if (i==p1)
                {
                    v.push_back(x);
                }
            }

    int ans=0;int xxx;
    scanf("%d",&p2);
    for (int i=1;i<=4;++i)
        for (int j=1;j<=4;++j)
            {
                scanf("%d",&x);
                if (i==p2)
                {
                    for (int k=0;k<4;++k) if (v[k]==x)
                    {
                        ++ans;
                        xxx=x;
                    }
                }
            }

    if (ans==1) printf("Case #%d: %d\n",++ca,xxx);
    if (ans==0) printf("Case #%d: Volunteer cheated!\n",++ca);
    if (ans>1) printf("Case #%d: Bad magician!\n",++ca);
}

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);

    int t;scanf("%d",&t);
    while (t--) work();

    fclose(stdin);
    fclose(stdout);
}
