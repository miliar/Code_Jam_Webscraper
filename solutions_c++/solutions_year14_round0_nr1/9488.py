#include<stdio.h>
#include<cstdlib>
int main()
{
    
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    
    int cases;
    int r;
    int cnt;
    int ans;
    int line1[4];
    int line2[4];
    scanf("%d",&cases);
    for(int ca=1;ca<=cases;ca++){
        scanf("%d",&r);
        for(int i=1;i<=4;i++){
            if(r==i){
                for(int j=0;j<4;j++) scanf("%d",&line1[j]);
            }
            else{
                for(int j=0;j<4;j++) scanf("%*d");
            }
        }
        scanf("%d",&r);
        for(int i=1;i<=4;i++){
            if(r==i){
                for(int j=0;j<4;j++) scanf("%d",&line2[j]);
            }
            else{
                for(int j=0;j<4;j++) scanf("%*d");
            }
        }
        cnt=0;
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                if(line1[i]==line2[j]){
                    cnt++;
                    ans=line1[i];
                }
            }
        }
        if(cnt>1){
            printf("Case #%d: Bad magician!\n",ca);
        }else if(cnt==0){
            printf("Case #%d: Volunteer cheated!\n",ca);
        }else{
            printf("Case #%d: %d\n",ca,ans);
        }
    }
}
