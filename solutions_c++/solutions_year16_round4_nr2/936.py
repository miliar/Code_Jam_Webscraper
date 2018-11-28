#include <cstdio>
#include <algorithm>

using namespace std;

int T,n,k;
double p[201];

FILE *in, *out;

int main()
{
    in = fopen("B-small-attempt0.in","r");
    out = fopen("B-small.out","w");

    fscanf(in,"%d",&T);
    for(int t=1; t<=T; t++) {
        fscanf(in,"%d%d",&n,&k);
        for(int i=0; i<n; i++) fscanf(in,"%lf",&p[i]);

        double maxx(0);

        for(int i=0; i<(1<<n); i++) {
            double cc[(k/2)+1];
            fill(cc,cc+(k/2)+1,0);
            cc[0] = 1.0;

            int db(0);
            for(int j=0; j<n; j++) {
                if(i&(1<<j)) {
                    db++;

                    for(int l=k/2; l>0; l--) cc[l] = (cc[l-1]*p[j]) + (cc[l]*(1.0-p[j]));
                    cc[0] *= (1.0-p[j]);
                }
            }
            if(db!=k) continue;
            maxx = max(maxx,cc[k/2]);
        }


        fprintf(out,"Case #%d: %lf\n",t,maxx);
    }

    fclose(in);
    fclose(out);

    return 0;
}
