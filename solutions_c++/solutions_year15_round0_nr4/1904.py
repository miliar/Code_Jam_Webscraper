#include <cstdio>
int t;
int main()
{

        FILE *inf = fopen("D.in","r");
        //FILE *inf = stdin;
        //FILE *outf = stdout;
        FILE *outf = fopen("D.out","w");

        fscanf(inf,"%d",&t);
        for (int i=1; i <= t; ++i) {
                int x,r,c;
                fscanf(inf, "%d%d%d", &x, &r, &c);
                bool ans = true;
                if (r < c) {
                        int tmp = r;
                        r = c;
                        c = tmp;
                }
                for (int j=1; j<=x; ++j) {
                        int k = x-j+1;
                        if ( (k > r || j > c) && (k > c || j > r)) {
                                ans = false;
                                break;
                        }
                }
                if(x==4 && r<=4 && c<=2) ans=false;
                if (r*c % x)
                        ans = false;

                fprintf(outf,"Case #%d: %s\n", i, ans?"GABRIEL":"RICHARD");

        }
}
