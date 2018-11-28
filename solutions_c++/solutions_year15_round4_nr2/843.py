#include<cstdio>
#include<algorithm>
#include<cmath>
#define rate second
#define temp first
#define eps 0.00000001
using namespace std;

long double V, X;
pair<long double, long double> S[250];
int n;

int main() {
    int Z;
    scanf("%d", &Z);
    for(int zz = 1; zz <= Z; ++zz) {
        scanf("%d %Lf %Lf", &n, &V, &X);
        //printf("targetV = %Lf, targetX = %Lf\n", V, X);
        for(int i = 0; i < n; ++i) {
            long double a, b;
            scanf("%Lf %Lf", &a, &b);
            S[i] = make_pair(b, a);
            //printf("temp = %Lf rate = %Lf\n", S[i].temp, S[i].rate);
        }
        bool alllower = true, allhigher = true;
        for(int i = 0; i < n; ++i) {
            if (X - S[i].temp > -eps) allhigher = false;
            if (S[i].temp - X > -eps) alllower = false;
        }
        if (alllower || allhigher) {
            printf("Case #%d: IMPOSSIBLE\n", zz);
            continue;
        }
        sort(S, S+n);
        long double p = 0, q = 1e7;
        while(q - p > eps) {
            long double t = (p+q)/2;
            long double currV = 0, currVX = 0;
            for (int i = 0; i < n; ++i) {
                currV += S[i].rate * t;
                currVX += S[i].rate*S[i].temp*t;
            }
            //printf("t=%Lf cV=%Lf cVX=%Lf cX=%Lf\n", t, currV, currVX, currVX/currV);
            if (X - currVX / currV > eps) {
                //printf("too cold\n");
                for(int i = 0; X - currVX / currV > eps && X - S[i].temp > eps; i++) {
                    if (X - (currVX - S[i].rate*t*S[i].temp) / (currV - S[i].rate*t) > eps) {
                        currV -= S[i].rate*t;
                        currVX -= S[i].rate*t*S[i].temp;
                    } else {
                        long double md = (X*currV - currVX) / (X*S[i].rate - S[i].rate*S[i].temp);
                        currV -= S[i].rate*md;
                        currVX -= S[i].rate*md*S[i].temp;
                    }
                }
            }
            else {
                //printf("too hot\n");
                 for(int i = n-1; currVX / currV - X > eps && S[i].temp - X > eps; i--) {
                    if ((currVX - S[i].rate*t*S[i].temp) / (currV - S[i].rate*t) - X > eps) {
                        currV -= S[i].rate*t;
                        currVX -= S[i].rate*t*S[i].temp;
                    } else {
                        long double md = (X*currV - currVX) / (X*S[i].rate - S[i].rate*S[i].temp);
                        currV -= S[i].rate*md;
                        currVX -= S[i].rate*md*S[i].temp;
                    }
                } 
            }
            //printf("after negation V=%Lf VX=%Lf X=%Lf\n", currV, currVX, currVX/currV);
            if(currV >= V) q = t;
            else p = t;
        }
        printf("Case #%d: %Lf\n", zz, (p+q)/2);
    }  
    return 0;
}
