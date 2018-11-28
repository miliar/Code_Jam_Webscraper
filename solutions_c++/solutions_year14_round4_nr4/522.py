#include<stdio.h>
#include<vector>
#include<string>
#include<math.h>
#include<algorithm>
using namespace std;

#define sz size()
#define pb push_back
#define len length()
#define clr clear()

#define eps 0.0000001
#define PI  3.14159265359

int m,n,resm,resk,g[555],brg[555];
string s[555];

void idar(int x) {

    int i,j,t,p,pp,bb;

    if (x == m) {
        t=0;
        for(i=0; i<n; i++) if (brg[i]>0) t++;
        for(i=0; i<m; i++) {
            pp = 0;
            //for(j=0; j<m; j++) if (i!=j && g[i] == g[j]) {
            //if (i>0) {
                j = i-1;
                while(j>=0 && g[i] != g[j]) j--;

                if (j>=0) {
                    p = 0;
                    while(p<s[j].length() && p<s[i].length() && s[i][p] == s[j][p]) p++;

                    if (p > pp) pp = p;
                }
            //}

            //printf("%d %d\n", i, pp);
            t += s[i].length() - pp;
        }

        if (t > resm) {
            /*printf("-> %d\n", t);
            for(i=0; i<m; i++) {
                printf("%s %d\n", s[i].c_str(), g[i]);
            }
            system("pause");*/
            resm = t;
            resk = 1;
        } else if (t == resm) {
            resk++;
        }

        return;
    }

    for(i=0; i<n; i++) {
        g[x] = i;
        brg[i]++;
        idar(x+1);
        brg[i]--;
    }
}

int main() {

    FILE *ff=fopen("D-small-attempt0.in", "r"), *gg=fopen("D-small-attempt0.out", "w");

    int i,tt,ttt;
    char ps[555];

    fscanf(ff,"%d", &ttt);
    for(tt=1;tt<=ttt;tt++) {
        fprintf(gg,"Case #%d: ", tt);

        fscanf(ff,"%d%d", &m, &n);

        for(i=0; i<m; i++) {
            fscanf(ff,"%s", &ps);
            s[i] = string(ps);
        }

        sort(s,s+m);
        for(i=0; i<n; i++) brg[i]=0;
        resm = -1; resk = 0;
        idar(0);

        fprintf(gg, "%d %d\n", resm, resk);
    }

    fclose(ff); fclose(gg);

    return 0;
}
