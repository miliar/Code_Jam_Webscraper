#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <set>
#include <map>

using namespace std;


int main()
{
    freopen("A-small-attempt3.in","r",stdin);
    freopen("output.out","w",stdout);
    int t;
    scanf("%d",&t);

    for (int k(0);k<t;k++)
    {
    int tmp;
    bool bad(false);
    vector<int> rjes(17,0);
    int karte[4][4];
    for(int j(0);j<2;j++)
    {
    scanf("%d",&tmp);
    for(int i(0);i<4;i++) scanf("%d %d %d %d",&karte[i][0],&karte[i][1],&karte[i][2],&karte[i][3]);
    for(int i(0);i<4;i++) rjes[karte[tmp-1][i]]++;
    }
    int ans(0);
    for(int i(1);i<17;i++)
    {
        if(rjes[i]>1 && bad) {ans=-100; break; }
        else if(rjes[i]>1 && !bad) {ans=i; bad=true;}
    }
        if(ans<0) {printf("Case #%d: Bad magician!\n",k+1);}
        else if(bad && ans>0) {printf("Case #%d: %d\n",k+1,ans);}
        else if (!bad) printf("Case #%d: Volunteer cheated!\n",k+1);
    }

    return 0;
}
