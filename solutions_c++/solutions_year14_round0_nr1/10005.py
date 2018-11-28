#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int main()
{
    //freopen("A-small-attempt0.in","r",stdin);
    //freopen("out.txt","w",stdout);
    int tcase,t=0;
    scanf("%d",&tcase);
    while(tcase--){
        t++;
        int count[17];
        memset(count,0,sizeof(count));
        int fRow,sRow;
        scanf("%d",&fRow);
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                int temp;
                scanf("%d",&temp);
                if(fRow-1==i)count[temp]++;
            }
        }
        scanf("%d",&sRow);
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                int temp;
                scanf("%d",&temp);
                if(sRow-1==i)count[temp]++;
            }
        }
        int ans=0,value;
        for(int i=0;i<17;i++){
            if(count[i]==2)ans++,value=i;
        }
        if(ans==0)printf("Case #%d: Volunteer cheated!\n",t);
        else if(ans==1)printf("Case #%d: %d\n",t,value);
        else printf("Case #%d: Bad magician!\n",t);
    }
    return 0;
}
