#include<stdio.h>
#include<stdlib.h>

using namespace std;
int fir[4],sec[4];





int main(){

    int x,a,a1,a2,a3,a4,cnt,ans,cas=1;
    int i,j;
    scanf("%d",&x);
    while(x--){
        scanf("%d",&a);
        for(i=0;i<4;i++){
            scanf("%d%d%d%d",&a1,&a2,&a3,&a4);
            if(i==a-1){
                fir[0]=a1;
                fir[1]=a2;
                fir[2]=a3;
                fir[3]=a4;
            }
        }
        scanf("%d",&a);
        for(i=0;i<4;i++){
            scanf("%d%d%d%d",&a1,&a2,&a3,&a4);
            if(i==a-1){
                sec[0]=a1;
                sec[1]=a2;
                sec[2]=a3;
                sec[3]=a4;
            }
        }
        for(i=0,cnt=0;i<4;i++){
            for(j=0;j<4;j++){
                if(fir[i]==sec[j]){
                    cnt++;
                    ans=fir[i];
                }
            }
        }
        if(cnt==0)
            printf("Case #%d: Volunteer cheated!\n",cas++);
        else if(cnt==1)
            printf("Case #%d: %d\n",cas++,ans);
        else
            printf("Case #%d: Bad magician!\n",cas++);

    }


    return 0;
}
