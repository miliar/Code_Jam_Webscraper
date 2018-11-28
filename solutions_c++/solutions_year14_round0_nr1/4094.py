#include<iostream>
#include<cstdio>

using namespace std;

int g, n, w, t[20], t1[10], t2[10], x, y, z;
int main() {
    int i, j, k;
    scanf("%d", &g);
    for (i=1; i<=g; ++i) {
        scanf("%d", &w);
        for (j=0; j<16; ++j) {
            scanf("%d", &t[j]);
        }
        x=(w-1)*4;
        for (j=x; j<x+4; ++j) {
            t1[j-x+1]=t[j];
                            //cout<<"   t1["<<j-x+1<<"]: "<<t1[j-x+1]<<endl;
        }
        scanf("%d", &w);
        for (j=0; j<16; ++j) {
            scanf("%d", &t[j]);
        }
        x=(w-1)*4;
        for (j=x; j<x+4; ++j) {
            t2[j-x+1]=t[j];
                            //cout<<"   t2["<<j-x+1<<"]: "<<t2[j-x+1]<<endl;
        }
        y=0;
        for (j=1; j<=4; ++j) {
            for (k=1; k<=4; ++k) {
                if (t1[j]==t2[k]) {
                    y++;
                    z=j;
                }
            }
        }
        if (y==0) {
            printf("Case #%d: Volunteer cheated!\n", i);
        }
        if (y==1) {
            printf("Case #%d: %d\n", i, t1[z]);
        }
        if (y>1) {
            printf("Case #%d: Bad magician!\n", i);
        }
    }
    return 0;
}
