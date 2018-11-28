#include <stdio.h>
#include <stdlib.h>
#include <set>
#include <algorithm>

using namespace std;

void showset(const char* name, set<int> s)
{
    set<int>::iterator it;
    printf("%s:  ",name);
    for(it=s.begin();it!=s.end();it++)
    {
        printf("%d  ",*it);
    }
    printf("\n");
}

int main()
{
    int t,c0,c1,grid0[4][4],grid1[4][4];

    freopen ("A-small-attempt0.out","w",stdout);
    freopen ("A-small-attempt0.in","r",stdin);

    scanf("%d",&t);
    for (int i=1;i<=t;i++)
    {
        scanf("%d",&c0);
        for (int j=0;j<4;j++) scanf("%d%d%d%d",&grid0[j][0],&grid0[j][1],&grid0[j][2],&grid0[j][3]);
        scanf("%d",&c1);
        for (int j=0;j<4;j++) scanf("%d%d%d%d",&grid1[j][0],&grid1[j][1],&grid1[j][2],&grid1[j][3]);

        set<int>s0;
        set<int>s1;
        set<int>res;

        s0.clear();
        for (int j=0;j<4;j++) s0.insert(grid0[c0-1][j]);
        s1.clear();
        for (int j=0;j<4;j++) s1.insert(grid1[c1-1][j]);
        set_intersection(s0.begin(),s0.end(),s1.begin(),s1.end(),inserter(res,res.begin()));

        //showset("s0",s0);
        //showset("s1",s1);
        //showset("res",res);

        set<int>::iterator is;
        if (res.size()==0)
        {
            is = res.begin();
            printf("Case #%d: Volunteer cheated!\n",i);
        }
        if (res.size()==1)
        {
            is = res.begin();
            printf("Case #%d: %d\n",i,*is);
        }
        if (res.size()>1)
        {
            is = res.begin();
            printf("Case #%d: Bad magician!\n",i);
        }
    }

    //system("pause");

    return 0;
}
