#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
int s1[5][5],s2[5][5];
int main()
{
    freopen("A-small-attempt5.in","r",stdin);
    freopen("a.txt","w",stdout);
    int cas,hhcas,a,b;
    scanf("%d",&hhcas);
    for (int cas=1;cas<=hhcas;++cas)
    {
        int num=0,ans;
        scanf("%d",&a);
        for (int i=0;i<4;++i)
            for (int j=0;j<4;++j)
                scanf("%d",&s1[i][j]);
        scanf("%d",&b);
        for (int i=0;i<4;++i)
            for (int j=0;j<4;++j)
                scanf("%d",&s2[i][j]);
        for (int i=0;i<4;++i)
            for (int j=0;j<4;++j)
                if (s1[a-1][i]==s2[b-1][j])
                {
                    num++;
                    //cout<<"................."<<s1[a-1][i]<<endl;
                    ans=s1[a-1][i];
                }
                //cout<<"................."<<s1[a-1][i]<<endl;
        if (num==1)
            printf("Case #%d: %d\n",cas,ans);
        else if (num==0)
            printf("Case #%d: Volunteer cheated!\n",cas);
        else
            printf("Case #%d: Bad magician!\n",cas);
    }
    return 0;
}
