#include <stdio.h>
int main(){

    int f;
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&f);
    int a[4],b[4];
    int temp = 0;
    while(f--){
        int row1,row2;
        int count = 0;
        int ans;
        scanf("%d",&row1);
        for(int i = 0; i < 4; i++){
            if(row1 == i+1){
                for(int j=0;j<4;j++){
                    scanf("%d",&a[j]);
                }
            }else{
                for(int j=0;j<4;j++){
                    int hold;
                    scanf("%d",&hold);
                }
            }
        }
        scanf("%d",&row2);
        for(int i=0;i<4;i++){
            if(row2 == i+1){
                for(int j=0;j<4;j++){
                    scanf("%d",&b[j]);

                }
            }else{
                for(int j=0;j<4;j++){
                    int hold;
                    scanf("%d",&hold);
                }
            }
        }
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                if(a[i]==b[j]){
                    count++;
                    ans = a[i];
                }
            }
        }
        if(count==1){
            printf("Case #%d: %d\n",++temp,ans);
        }else if(count>1){
            printf("Case #%d: Bad magician!\n",++temp);
        }else{
            printf("Case #%d: Volunteer cheated!\n",++temp);
        }

    }
    return 0;
}
