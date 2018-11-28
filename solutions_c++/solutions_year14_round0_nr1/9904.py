#include<algorithm>
#include<cstdio>
#include<iostream>
using namespace std;

int A[4][4],B[4][4];

int main(){
    int a,b,count,t,i,j,k=1;
    scanf("%d",&t);

    while(t--){
        scanf("%d",&a);

        for(i=0;i<4;++i)
            for(j=0;j<4;++j)
                scanf("%d",&A[i][j]);

        scanf("%d",&b);

        for(i=0;i<4;++i)
            for(j=0;j<4;++j)
                scanf("%d",&B[i][j]);

        count = 0;
        int nn;
        for(i=0;i<4;++i)
            for(j=0;j<4;++j)
                if(A[a-1][i] == B[b-1][j]){
                    count++;
                    nn = A[a-1][i];
                }
       // printf("Case #%d: ",k++);
        if(count == 1)
            printf("Case #%d: %d\n",k++,nn);
        else if(count>1)
            printf("Case #%d: Bad magician!\n",k++);
        else
            printf("Case #%d: Volunteer cheated!\n",k++);
    }
    return 0;
}
