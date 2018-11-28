#include<iostream>
#include<stdio.h>
using namespace std;

int main(){
    int cases=0,a[4][4],b[4][4],i,j,count,c,t=1,p,q;
    freopen("A-small-attempt1.in","r",stdin);
    freopen("output1.txt", "w", stdout);
    scanf("%d",&cases);
    while(cases--){
            count=0;
        scanf("%d",&p);
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                scanf("%d",&a[i][j]);
            }
        }

        scanf("%d",&q);
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                scanf("%d",&b[i][j]);
            }
        }

        for(i=0;i<4;i++){
             for(j=0;j<4;j++){
                if(a[p-1][i]==b[q-1][j])
                    {
                        c = a[p-1][i];
                        count++;}
             }
        }
        if(count==1) printf("Case #%d: %d\n",t,c);
        if(count>1) printf("Case #%d: Bad magician!\n",t);
        if(count<1) printf("Case #%d: Volunteer cheated!\n",t);
        t++;
    }

return 0;
}
