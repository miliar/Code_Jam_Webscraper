#include<cstdio>
int T,a,b[20][5],x,ac,cnt;
int main(){
    scanf("%d",&T);
    for (int o=1; o<=T; o++){
        ac=-1; cnt=0;
        scanf("%d",&x);
        for (int i=1; i<=16; i++) b[i][1]=0;
        for (int i=1; i<=4; i++)
            for (int j=1; j<=4; j++){
                scanf("%d",&a);
                if (i==x) b[a][1]=1;
            }
        scanf("%d",&x);
        for (int i=1; i<=16; i++) b[i][2]=0;
        for (int i=1; i<=4; i++)
            for (int j=1; j<=4; j++){
                scanf("%d",&a);
                if (i==x) b[a][2]=1;
            }
        for (int i=1; i<=16; i++) 
            if (b[i][1]&&b[i][2]) ac=i,++cnt;
        printf("Case #%d: ",o);
        if (cnt==1) printf("%d\n",ac);
        else if (cnt==0) printf("Volunteer cheated!\n");
        else printf("Bad magician!\n");
    }
    return 0;    
}
