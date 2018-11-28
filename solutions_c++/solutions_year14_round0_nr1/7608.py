#include <iostream>
#include <stdio.h>
#include <math.h>

using namespace std;

int main()
{
    int t;
    scanf("%d\n",&t);
    for (int i=0; i<t; i++) {
        int r1,r2,a[4],x[4],j,y[4];
        printf("Case #%d: ",i+1);
        scanf("%d\n",&r1);
        for (j=0; j<4; j++) {
            scanf("%d %d %d %d\n",&a[0],&a[1],&a[2],&a[3]);
            //printf("X: %d %d %d %d\n",a[0],a[1],a[2],a[3]);
            if(j+1==r1) {
                x[0]=a[0];
                x[1]=a[1];
                x[2]=a[2];
                x[3]=a[3];
            }
        }
        //printf("X: %d %d %d %d\n",x[0],x[1],x[2],x[3]);

        scanf("%d\n",&r2);
        for (j=0; j<4; j++) {
            scanf("%d %d %d %d\n",&a[0],&a[1],&a[2],&a[3]);
            if(j+1==r2) {
                y[0]=a[0];
                y[1]=a[1];
                y[2]=a[2];
                y[3]=a[3];
            }
        }
        //printf("Y: %d %d %d %d\n",y[0],y[1],y[2],y[3]);
        int num=0;
        for (j=0; j<4; j++) {
            for (int k=0; k<4; k++) {
                if (x[j]==y[k]) {
                    if (!num) {
                        num=x[j];
                    }
                    else num=17;
                }
            }
        }
        if (num==0) {
            printf("Volunteer cheated!\n");
        }
        else if(num==17) {
            printf("Bad magician!\n");
        }
        else
            printf("%d\n",num);
    }
}