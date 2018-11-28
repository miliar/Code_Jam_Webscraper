#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int num[2][5][5];
int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    //freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for(int cas=1;cas<=t;cas++)
    {
        printf("Case #%d: ",cas);
        int ans1;
        cin>>ans1;
        ans1--;
        for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
            cin>>num[0][i][j];
        int ans2;
        cin>>ans2;
        ans2--;
        for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
            cin>>num[1][i][j];
        int ans=0;
        for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
        {
            if(num[0][ans1][i]==num[1][ans2][j])
            {
                if(ans>0)
                {
                    ans=-1;
                }
                else if(ans==0)
                {
                    ans=num[0][ans1][i];
                }
            }
        }
        if(ans>0)
            printf("%d\n",ans);
        else if(ans==0)
        {
            printf("Volunteer cheated!\n");
        }
        else printf("Bad magician!\n");
    }
}
