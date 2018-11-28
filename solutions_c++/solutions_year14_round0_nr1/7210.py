#include<cstdio>
int main() {
    int t,z;
    scanf("%d",&t);
    for(z=1;z<=t;z++){
        int A[4][4]={0},a[4],p=0;
        int B[4][4]={0},b[4],q=0;
        int c=0,x,y,r;
        scanf("%d",&x);
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                scanf("%d",&A[i][j]);
        scanf("%d",&y);
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                scanf("%d",&B[i][j]);
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                if(A[x-1][i]==B[y-1][j]){
                    c++;
                    r=A[x-1][i];
                }
        printf("Case #%d: ",z);
        if(c==1)
            printf("%d\n",r);
        else if(c==0)
            printf("Volunteer cheated!\n");
        else
            printf("Bad magician!\n");
    }
    return 0;
}
