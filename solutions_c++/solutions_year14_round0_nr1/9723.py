#include <iostream>
#include <cstdio>
using namespace std;
int main() {
    int t;
    scanf("%d",&t);
    for (int i=1;i<=t;i++) {
        int i1,i2,arr1[4][4],arr2[4][4];
        scanf("%d",&i1);
        for (int j=0;j<4;j++) {
            for (int k=0;k<4;k++) scanf("%d",&arr1[j][k]);
            }
        scanf("%d",&i2);
        for (int j=0;j<4;j++) {
            for (int k=0;k<4;k++) scanf("%d",&arr2[j][k]);
            }
        int count=0,sama;
        for (int j=0;j<4;j++) {
            for (int k=0;k<4;k++) {
                if (arr1[i1-1][j]==arr2[i2-1][k]) { 
                sama=arr1[i1-1][j];
                count++;
                }
                }
            }
        if (count==0) printf("Case #%d: Volunteer cheated!\n",i);
        else if (count>1) printf("Case #%d: Bad magician!\n",i);
        else printf("Case #%d: %d\n",i,sama);
        }
    }
