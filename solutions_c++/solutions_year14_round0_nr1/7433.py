#include <stdio.h>
#include <vector>
using namespace std;
int main()
{
    int totalcase;
    scanf("%d",&totalcase);
    for(int o=1;o<=totalcase;o++)
    {
        int possible[20]={0};
    int currow;
    int a[4][4];
    scanf("%d",&currow);
    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
            scanf("%d",&a[i][j]);
    for(int i=0;i<4;i++)
        possible[a[currow-1][i]]++;

    scanf("%d",&currow);
    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
            scanf("%d",&a[i][j]);
    for(int i=0;i<4;i++)
        possible[a[currow-1][i]]++;
    vector<int> ans;
    for(int i=0;i<20;i++) if(possible[i]==2) ans.push_back(i);
    printf("Case #%d: ",o);
    if(ans.size()==0) printf("Volunteer cheated!\n");
    else if(ans.size()>1) printf("Bad magician!\n");
    else printf("%d\n",ans[0]);
    }

}
