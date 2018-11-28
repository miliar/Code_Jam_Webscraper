#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
int a[26],b[10],cas;
char chr[2005];
int main(){
    freopen("A-large.in.txt","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    while(T--){
        memset(a,0,sizeof(a));
        memset(b,0,sizeof(b));
        scanf("%s",chr);
        for(int i=0;i<strlen(chr);i++){
            a[chr[i]-'A']++;
        }
        b[0]=a[25];
        b[2]=a[22];
        b[4]=a[20];
        b[6]=a[23];
        b[8]=a[6];
        b[1]=a[14]-b[0]-b[2]-b[4];
        b[3]=a[19]-b[2]-b[8];
        b[5]=a[5]-b[4];
        b[7]=a[18]-b[6];
        b[9]=a[8]-b[5]-b[8]-b[6];
        printf("Case #%d: ",++cas);
        for(int i=0;i<10;i++)
            for(int j=0;j<b[i];++j)
                printf("%d",i);
        puts("");
    }
    return 0;
}
/*
ABCDE
FGHIJ
KLMNO
PQRST
UVWXY
Z
*/