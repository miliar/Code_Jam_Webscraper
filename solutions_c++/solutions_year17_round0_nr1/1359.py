#include<cstdio>
FILE *in = fopen("A-large.in", "r");
FILE *out = fopen("output.out", "w");
int t, k;
char s[1010];
int main() {
    fscanf(in, "%d", &t);
    for(int l=1;l<=t;l++) {
        fscanf(in, "%s%d", s, &k);
        int i, r = 0;
        for(i=0;s[i+k-1];i++) {
            if(s[i] == '-') {
                for(int j=0;j<k;j++)
                    if(s[i+j] == '-') s[i+j] = '+';
                    else s[i+j] = '-';
                r++;
            }
        }
        bool f = 1;
        for(;s[i];i++) if(s[i] == '-') {
            f = 0;
            break;
        }
        fprintf(out, "Case #%d: ", l);
        if(f) fprintf(out, "%d\n", r);
        else fprintf(out, "IMPOSSIBLE\n");
    }
    fclose(out);
    return 0;
}
