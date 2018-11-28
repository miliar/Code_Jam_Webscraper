#include <stdio.h>
#include <memory.h>
#include <string.h>

using namespace std;

const int MAXL = 1000005;
int dp[MAXL];
int next[MAXL];
int n,l,t;
char str[MAXL];

int in( char x ){
    if ( x == 'a' ) return 1;
    if ( x == 'e' ) return 1;
    if ( x == 'i' ) return 1;
    if ( x == 'o' ) return 1;
    if ( x == 'u' ) return 1;
    return 0;
}

int solve(){
    int ans,i,j,k,c,left,right;
    l = strlen(str);
    k = 0;
    ans = 0;
    memset(dp,0,sizeof(dp));
    c = n;
    for ( i = 0; i <l;i++ ){
        if ( !in(str[i]) ){
            c--;
            if ( c == 0 ) {
                dp[i-n+1] = 1;
                k++;
                next[k] = i-n+1;
                c++;
            }
        }else{
            dp[i] = 0;
            c = n;
        }
    }
    j = 0;
    c = l;
    ans = 0;
    for ( i = 1; i <= k; i++ ){
        printf("next %d\n",next[i]);
    }

    for ( i = 1; i <= k; i++ ){
        left = next[i]-j;
        right = l-next[i]-n;
        printf("%d %d\n",left,right);
        ans += (right+1)*(left+1);
        j = next[i]+1;
    }
    printf("ans = %d\n",ans);
    return ans;
}

main(){
    int cas,i;
    FILE* fin = fopen("d:\\g.in","r");
    FILE* fout = fopen("d:\\out.txt","w");
    fscanf(fin,"%d",&t);
    for ( cas = 1; cas <= t; cas++ ){
        fscanf(fin,"%s %d",str,&n);
        fprintf(fout,"Case #%d: %d\n",cas,solve());
    }
    fclose(fin);
    fclose(fout);
}
