#include<iostream>
#include<cstdio>

using namespace std;

inline int common(int a[], int b[], int &ans) {
    int i, j, flag=0;
    for(i=0; i<4; i++) {
        for(j=0; j<4; j++) {
            if(a[i]==b[j]) {
                if(flag == 0) {
                    flag = 1;
                    ans = a[i];
                }
                else {
                    return 2;
                }
            }
        }
    }
    if(flag==1) {
        return 1;
    }
    else return 0;
}

int main() {
    int t;
    scanf("%d", &t);
    int a[4][4], b[4][4];

    for(int k=1; k<=t; k++) {

        int x,y,i,j,p,ans;

        scanf("%d", &x);
        for(i=0; i<4; i++) {
            for(j=0; j<4; j++) {
                scanf("%d", &a[i][j]);
            }
        }
        scanf("%d", &y);
        for(i=0; i<4; i++) {
            for(j=0; j<4; j++) {
                scanf("%d", &b[i][j]);
            }
        }

        p = common(a[x-1], b[y-1], ans);

        if(p==1) {
            printf("Case #%d: %d\n", k, ans);
        }
        else if(p>1) {
            printf("Case #%d: Bad magician!\n", k);
        }
        //p==0
        else {
            printf("Case #%d: Volunteer cheated!\n", k);
        }

    }
    return 0;
}
