#include <cstdio>

using namespace std;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int a,b,c,i,j,k,tmp1[16],tmp2[16];
    scanf("%d",&a);
    for(k=1;k<=a;k++){
        int cnt=0,ans;
        scanf("%d",&b);
        for(i=0;i<16;i++){
            scanf("%d",&tmp1[i]);
        }
        scanf("%d",&c);
        for(i=0;i<16;i++){
            scanf("%d",&tmp2[i]);
        }
        for(i=(b-1)*4;i<b*4;i++){
            for(j=(c-1)*4;j<c*4;j++){
                if(tmp1[i]==tmp2[j]){
                    cnt++;
                    ans=tmp1[i];
                }
                if(cnt==2) break;
            }
            if(cnt==2) break;
        }
        printf("Case #%d: ",k);
        if(cnt==0){
            puts("Volunteer cheated!");
        }
        else if(cnt==1){
            printf("%d\n",ans);
        }
        else{
            puts("Bad magician!");
        }
    }
    return 0;
}
