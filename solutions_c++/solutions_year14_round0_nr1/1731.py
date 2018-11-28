#include <iostream>
using namespace std;
#include <stdio.h>
#include <string>
#include <algorithm>
#include <string.h>

int A[4][4],B[4][4];
bool run[17];
int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cnt = 1;cnt<=T;cnt++)
    {
        cerr<<cnt<<endl;
        int ans = -1;
        int r1,r2;
        memset(run,false,sizeof(run));
        scanf("%d",&r1);
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++) scanf("%d",&A[i][j]);
        scanf("%d",&r2);
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++) scanf("%d",&B[i][j]);
        r1--;
        r2--;
        for(int i=0;i<4;i++)
            run[A[r1][i]]=true;
        for(int i=0;i<4;i++)
        {
            if(run[B[r2][i]]==true)
            {
                if(ans==-1) ans = B[r2][i];
                else if(ans>0) { ans = 0;  break ;}
            }
        }
        printf("Case #%d: ",cnt);
        if(ans==0) printf("Bad magician!\n");
        else if(ans==-1) printf("Volunteer cheated!\n");
        else printf("%d\n",ans);
    }
    return 0;
}
