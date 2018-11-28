#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

int mat1[10][10],mat2[10][10];

int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("A-small-attempt0.in","r",stdin);
    //freopen("out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++)
    {
        int first,second;
        scanf("%d",&first);
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
                scanf("%d",&mat1[i][j]);
        scanf("%d",&second);
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
                scanf("%d",&mat2[i][j]);
        vector<int> ans;
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
                if(mat1[first][i]==mat2[second][j])
                {
                    ans.push_back(mat1[first][i]);
                    break;
                }
        printf("Case #%d: ",cas);
        if(ans.empty())
            puts("Volunteer cheated!");
        else if(ans.size()==1)
            printf("%d\n",ans[0]);
        else
            puts("Bad magician!");
    }
    return 0;
}
