#include<stdio.h>
#include<string>
#include<math.h>

using namespace std;


int clc( long long x ){
    int temp[10];
    int l,i;
    int r = (int)(sqrt(x));
    if ( r*r != x ) return 0;
    l = 1;
    printf("%d\n",r);
    
    while ( r != 0 ){
        temp[l] = r%10;
        r = r/10;
        printf("%d %d\n",l,temp[l]);
        l++;
    }
    printf("l = %d\n",l);
    l --;
    for ( i = 1; i <= (l+1)/2; i++ ){
        if ( temp[i] != temp[l+1-i] ) return 0;
    }
    printf("~~~\n");
    l = 1;
    while ( x != 0 ){
        temp[l] = x%10;
        x = x/10;
        printf("%d %d\n",l,temp[l]);
        l++;
    }
    printf("l = %d\n",l);
    l -- ;
    for ( i = 1; i <= (l+1)/2; i++ ){
        if ( temp[i] != temp[l+1-i] ) return 0;
    }
    printf("final\n");
    return 1;
}

int main(){
    FILE* fin = fopen("d:\\g2.in","r");
    FILE* fout = fopen("d:\\ans.txt","w");
    int t,ans;
    int i,a,b,j;
    fscanf(fin,"%d",&t);
    for ( i = 1; i <= t; i++){
        fscanf(fin,"%d%d",&a,&b);
        ans = 0;
        for ( j = a; j <= b; j++ ){
            ans += clc(j);
        }
        fprintf(fout,"Case #%d: %d\n",i,ans);
    }
    fclose(fin);
    fclose(fout);
    getchar();

}
