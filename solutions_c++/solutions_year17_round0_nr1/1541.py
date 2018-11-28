#include<stdio.h>
#include<string.h>
int T;
int n,m;
char c[1011];
int a[1011];
int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large-out.txt","w",stdout);
    int i,j,k;
    int p,q,r;

scanf("%d",&T);
for(int ii=0; ii<T;ii++) {
    scanf("%s",c);
    scanf("%d",&m);
    n = strlen(c);
    for(i=0;i<n;i++) {
        if(c[i] == '-') a[i] = 0;
        else if(c[i] == '+') a[i] = 1;
    }
    p = 0;
    for(i=0;i<n;i++) {
        if(i + m > n) break;
        if(a[i] == 0) {
            p ++;
            for(j=0;j<m;j++) a[i+j] = (a[i+j] + 1) % 2;
        }
        //for(int iii=0;iii<n;iii++)printf(" %d",a[iii]);printf("\n");
    }
    k = 0;
    for(i=0;i<n;i++) {
        if(a[i] == 0) k = 1;
    }
    printf("Case #%d: ", ii + 1);
    if(k == 1) printf("IMPOSSIBLE\n");
    else printf("%d\n",p);
}

    return 0;
}
