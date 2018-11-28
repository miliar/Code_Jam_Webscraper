#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<cmath>
using namespace std;
int aa[10][10],bb[10][10];
int main()
{
    #ifndef ONLINE_JUDGE
        freopen("A-small-attempt0.in","r" ,stdin);
        freopen("out.txt","w" ,stdout);
    #endif // ONLINE_JUDGE


    int a,b,t,cas=0;

    scanf("%d",&t);
    while(t--){
        scanf("%d",&a);
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
            scanf("%d",&aa[i][j]);
        scanf("%d",&b);
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
            scanf("%d",&bb[i][j]);
            int sum = 0,ans;
            for(int i=0;i<4;i++)
                for(int j=0;j<4;j++)
                if(aa[a-1][i]==bb[b-1][j]){
                    ans = aa[a-1][i];
                    sum++;
                }
            if(sum==1){
                     printf("Case #%d: %d\n",++cas,ans);
            }
            else if(sum>1){
                     printf("Case #%d: Bad magician!\n",++cas);
            }
            else if(sum==0){
                   printf("Case #%d: Volunteer cheated!\n",++cas);
            }
    }
    return 0;
}
