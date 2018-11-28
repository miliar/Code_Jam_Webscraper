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

int off,t[555],a[1555333];
char ch[] = {'P', 'R', 'S'};

void idar(int k, int pos, int pob) {

    if (k == 0) {
        //printf("%d -> %d\n", pos-off, pob);
        t[pob]++;
        a[pos-off] = pob;
        return;
    }

    if (pob == 0) {
        idar(k-1,pos*2, 0);
        idar(k-1,pos*2 + 1, 1);
    } else if (pob == 1) {
        idar(k-1,pos*2, 1);
        idar(k-1,pos*2 + 1, 2);
    } else {
        idar(k-1,pos*2, 0);
        idar(k-1,pos*2+1, 2);
    }

}

void idarsort(int k, int l, int r) {
    if (k == 1) {
        if (a[l] > a[r]) {
            swap(a[l],a[r]);
        }
        return;
    }

    int m,i,bb;

    m = (l+r)/2;
    idarsort(k-1,l,m);
    idarsort(k-1,m+1,r);

    bb = false;
    for(i=l; i<=m; i++) {
        if (a[i]==a[m+1+i-l]) continue;
        if (a[i]>a[m+1+i-l]) {
            bb=true;
            break;
        } else {
            break;
        }
    }

    if (bb) {
        for(i=l; i<=m; i++) swap(a[i],a[m+1+i-l]);
    }
}

int main() {

    FILE *ff=fopen("A-large.in", "r"), *gg=fopen("A-large.out", "w");

    int n,r,p,s,i,tt,ttt;

    fscanf(ff,"%d", &ttt);
    for(tt=1;tt<=ttt;tt++) {
        fprintf(gg,"Case #%d: ", tt);

        //printf("asdasd %d\n", tt);

        fscanf(ff,"%d%d%d%d", &n, &r, &p, &s);

        off = 1<<n;

        t[0] = t[1] = t[2] = 0;
        idar(n,1,0);
        if (t[0] == p && t[1] == r && t[2] == s) {
            idarsort(n,0,off-1);
            for(i=0; i<off; i++) { fprintf(gg, "%c", ch[a[i]]); }
            fprintf(gg, "\n");
            continue;
        }

        //printf("ok\n");

        t[0] = t[1] = t[2] = 0;
        idar(n,1,1);
        if (t[0] == p && t[1] == r && t[2] == s) {
            idarsort(n,0,off-1);
            for(i=0; i<off; i++) fprintf(gg, "%c", ch[a[i]]);
            fprintf(gg, "\n");
            continue;
        }

        t[0] = t[1] = t[2] = 0;
        idar(n,1,2);
        if (t[0] == p && t[1] == r && t[2] == s) {
            idarsort(n,0,off-1);
            for(i=0; i<off; i++) fprintf(gg, "%c", ch[a[i]]);
            fprintf(gg, "\n");
            continue;
        }


        fprintf(gg, "IMPOSSIBLE\n");
    }

    fclose(ff); fclose(gg);

    return 0;
}
