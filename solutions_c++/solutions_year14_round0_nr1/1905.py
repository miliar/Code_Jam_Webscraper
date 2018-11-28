#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<vector>
using namespace std;

vector<int> ans;
int a[4][4],b[4][4];

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int TT;
    scanf("%d",&TT);
    for (int T=1;T<=TT;T++)
    {
        int row1,row2;
        scanf("%d",&row1);
        row1--;
        for (int i=0;i<4;i++)
            for (int j=0;j<4;j++)
                scanf("%d",&a[i][j]);
        scanf("%d",&row2);
        row2--;
        for (int i=0;i<4;i++)
            for (int j=0;j<4;j++)
                scanf("%d",&b[i][j]);
        ans.clear();
        for (int i=0;i<4;i++)
        {
            int flag=0;
            for (int j=0;j<4;j++)
                if (a[row1][i]==b[row2][j]) flag=1;
            if (flag) ans.push_back(a[row1][i]);
        }
        if (ans.size()==1) printf("Case #%d: %d\n",T,ans[0]);
        else if (ans.size()==0) printf("Case #%d: Volunteer cheated!\n",T);
        else printf("Case #%d: Bad magician!\n",T);
    }
    return 0;
}
