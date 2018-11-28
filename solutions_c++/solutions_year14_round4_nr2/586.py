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

struct st {
    int v,ind;
} a[5555];

bool cmp (st a, st b) {
    return a.v < b.v;
}

int b[5555];

int main() {

    FILE *ff=fopen("B-large.in", "r"), *gg=fopen("B-large.out", "w");

    int n,i,l,r,p,tt,ttt,pos,res,left,right;

    fscanf(ff,"%d", &ttt);
    for(tt=1;tt<=ttt;tt++) {
        fprintf(gg,"Case #%d: ", tt);

        fscanf(ff,"%d", &n);

        for(i=0; i<n; i++) {
            fscanf(ff,"%d", &a[i].v);
            a[i].ind = i;
        }

        sort(a,a+n,cmp);

        for(i=0; i<n; i++) {
            b[a[i].ind] = i;
        }

        res = 0;

        l = 0; r = n-1;

        for(i=0; i<n; i++) {
            pos=0;
            while(b[pos] != i) pos++;

            left = (pos - l) + 1;
            right = (r - pos) + 1;

            if (left < right) {
                while(pos>l) {
                    p = b[pos]; b[pos] = b[pos-1]; b[pos-1] = p;
                    pos--;
                    res++;
                }
                l++;
            } else {
                while (pos<r) {
                    p = b[pos]; b[pos] = b[pos+1]; b[pos+1] = p;
                    pos++;
                    res++;
                }
                r--;
            }
        }

        fprintf(gg, "%d\n", res);
    }

    fclose(ff); fclose(gg);

    return 0;
}
