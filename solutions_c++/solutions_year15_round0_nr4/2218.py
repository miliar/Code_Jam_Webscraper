#include<iostream>
#include<vector>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<cstdio>


using namespace std;

int nCases,x,r,c;

int main() {
    freopen("d.in","r",stdin);
    freopen("d.out","w",stdout);

    scanf("%d", &nCases);
    for(int cas=0;cas<nCases;cas++) {
        scanf("%d %d %d", &x, &r, &c);
        printf("Case #%d: ", cas+1);
        if(r>c) {
            int t=r;
            r=c;
            c=t;
        }
        if(x==1) {
            printf("GABRIEL\n");
        }
        else if(x==2) {
            if((r*c)%2==0) {
                printf("GABRIEL\n");
            } else {
                printf("RICHARD\n");
            }
        }
        else if (x==3) {
            if(c>=3 && r >=2 && (r*c)%3==0) {
                 printf("GABRIEL\n");
            } else {
                printf("RICHARD\n");
            }
        }
        else if (x==4) {
            if(c>=4 && r >=3 && (r*c)%4==0) {
                printf("GABRIEL\n");
            } else {
                printf("RICHARD\n");
            }
        }
        else if (x==5) {
            if(c>=5 && r >=3 && (r*c)%5==0) {
                printf("GABRIEL\n");
            } else {
                printf("RICHARD\n");
            }
        }
        else if (x==6) {
            if(c>=6 && r >=3 && (r*c)%6==0) {
                printf("GABRIEL\n");
            } else {
                printf("RICHARD\n");
            }
        }
        else if (x>=7) {
            printf("RICHARD\n");
        }
    }
}
