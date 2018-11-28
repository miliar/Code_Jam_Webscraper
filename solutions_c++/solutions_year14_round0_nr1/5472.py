#include<iostream>
#include<cstdio>
#include<cstring>
#include<vector>
using namespace std;

int kasus,a,b,ar[20];
vector <int> jawab;

int main()
{
//    freopen("A-small-attempt0.in","r",stdin);
//    freopen("a.out","w",stdout);
    
    scanf("%d",&kasus);
    for (int z=1;z<=kasus;z++)
    {
        memset(ar,0,sizeof(ar));
        for (int i=1;i<=2;i++)
        {
            scanf("%d",&a);
            for (int j=1;j<=4;j++)
                for (int k=1;k<=4;k++)
                {
                    scanf("%d",&b);
                    if (j==a) ar[b]++;
                }
        }
        jawab.clear();
        for (int i=1;i<=16;i++) if (ar[i]==2) jawab.push_back(i);
            
        printf("Case #%d: ",z);
        if (jawab.size()==1) printf("%d\n",jawab[0]);
        else if (jawab.size()==0) printf("Volunteer cheated!\n");
        else printf("Bad magician!\n");
    }
    return 0;
}
