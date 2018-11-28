#include <iostream>
#include <cstdio>

using namespace std;

int chose[10],chose2[10],card[5][5];

int main()
{
    int i,j,c,count,ans,N,a;
    scanf("%d",&N);
    for(c=1;c<=N;c++){
        count=0;
        scanf("%d",&a);
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                scanf("%d",&card[i][j]);
                if(i+1==a)chose[j]=card[i][j];
            }
        }
        scanf("%d",&a);
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                scanf("%d",&card[i][j]);
                if(i+1==a)chose2[j]=card[i][j];
            }
        }
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                if(chose[i]==chose2[j]){
                    count++;
                    ans=chose[i];
                }
            }
        }
        printf("Case #%d: ",c);
        if(count==1)printf("%d\n",ans);
        else if(count==0)printf("Volunteer cheated!\n");
        else printf("Bad magician!\n");
    }
    return 0;
}
