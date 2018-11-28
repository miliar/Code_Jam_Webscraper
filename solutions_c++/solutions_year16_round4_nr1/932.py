#include <cstdio>

using namespace std;

int possible(int n, int p, int r, int s) {
    if(!n) {
        if(p) return 0;
        if(r) return 1;
        if(s) return 2;
    }
    int pr = (1<<(n-1)) - s;
    int ps = (1<<(n-1)) - r;
    int rs = (1<<(n-1)) - p;

    if((pr<0) || (ps<0) || (rs<0)) return 5;
    return possible(n-1,pr,rs,ps);
}

int T,n;
int p,r,s;

FILE *in, *out;

char dp[13][3][(1<<12)+1];

bool kis(char *a, char *b) {
    if(*a=='\0') return 0;
    if(*a==*b) return kis(a+1,b+1);
    return (*a < *b);
}

void concat(char s[], char a[], char b[]) {
    int m(0);
    while(a[m]!='\0') {
        s[m] = a[m];
        m++;
    }
    int mm(0);
    while(b[mm]!='\0') {
        s[m] = b[mm];
        m++; mm++;
    }
    s[m] = '\0';
}

int main()
{
    dp[0][0][0] = 'P';
    dp[0][1][0] = 'R';
    dp[0][2][0] = 'S';
    dp[0][0][1] = dp[0][1][1] = dp[0][2][1] = '\0';
    for(int i=1; i<=12; i++) {
        for(int j=0; j<3; j++) {
            if(kis(&dp[i-1][j][0],&dp[i-1][(j+1)%3][0])) {
                concat(dp[i][j],dp[i-1][j],dp[i-1][(j+1)%3]);
            } else concat(dp[i][j],dp[i-1][(j+1)%3],dp[i-1][j]);
        }
    }


    in = fopen("A-large.in","r");
    out = fopen("A-large.out","w");

    fscanf(in,"%d",&T);
    for(int t=1; t<=T; t++) {
        fscanf(in,"%d%d%d%d",&n,&r,&p,&s);
        fprintf(out,"Case #%d: ",t);

        int pp = possible(n,p,r,s);

        if(pp == 5) {
            fprintf(out,"IMPOSSIBLE\n");
        } else {
            fprintf(out,"%s\n",dp[n][pp]);
        }
    }

    fclose(in);
    fclose(out);

    return 0;
}
