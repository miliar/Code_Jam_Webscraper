#include<cstdio>
#include<cstring>
int c[20],a[20][20];
int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int i,j,n,m,cs,csi;
    scanf("%d",&cs);
    for(csi=1;csi<=cs;csi++){
        scanf("%d",&n);
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
                scanf("%d",&a[i][j]);
        memset(c,0,sizeof(c));
        for(i=1;i<=4;i++)
            c[a[n][i]]++;
        scanf("%d",&n);
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
                scanf("%d",&a[i][j]);
        for(i=1;i<=4;i++)
            c[a[n][i]]++;
        j=-1;m=0;
        for(i=1;i<=16;i++)
        if(c[i]==2){
            m++;
            j=i;
        }
        printf("Case #%d: ",csi);
        if(m==0)puts("Volunteer cheated!");
        if(m==1)printf("%d\n",j);
        if(m>1)puts("Bad magician!");
    }
    return 0;
}

