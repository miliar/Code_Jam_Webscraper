#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>

using namespace std;

int fp[20],rp[20];
vector<int> res;
int main()
{
    int t,fi,se,a,cas=0;
    scanf("%d",&t);
    while(t--)
    {
        printf("Case #%d: ",++cas);
        res.clear();
        scanf("%d",&fi);
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                scanf("%d",&a);
                fp[a] = i;
            }
        }
        scanf("%d",&se);
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                scanf("%d",&a);
                rp[a] = i;
            }
        }
        for(int i=1;i<=16;i++)
        {
            if(fp[i]==fi&&rp[i]==se)
                res.push_back(i);
        }
        if(res.size()==1)
        {
            printf("%d\n",res[0]);
        }
        else if(res.size()==0)
        {
            puts("Volunteer cheated!");
        }
        else
        {
            puts("Bad magician!");
        }
    }
}
