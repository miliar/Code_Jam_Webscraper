#include <stdio.h>
#include <algorithm>
#include <iostream>

using namespace std;

int fairgame(double ken[], double naomi[], int n)
{
    int count = 0;
    int index = 0;
    int kw = 0;
    int nw = 0;
    int i, j;
    for (i = 0; i < n; i++) {
        for (j = i + index; j < n; j++) {
            if (ken[j] > naomi [i]) {
                         kw++;
                         break;
            }
            else {
                 index++;
            }
        }
    }
    count = n - kw;
    return count;
}


int cheating(double ken[], double naomi[], int n)
{
    int count = 0;
    int index = 0;
    int i, j;
    for (i = 0; i < n; i++) {
        for (j = i + index; j < n; j++) {
            if (naomi[i] > ken [j]) {
                         count++;
                         break;
            }
            else {
                 index++;
            }
        }
    }
    return count;
}


int main ()
{
    int z, i, j, t, n, f, c;
    double ken[1005], naomi[1005];
    scanf("%d", &t);
    for(z = 1; z <= t; z++) {
               scanf("%d", &n);
              for (i = 0; i < n; i++) {
                  scanf("%lf", &naomi[i]);
              }

              for (i = 0; i < n; i++) {
                  scanf("%lf", &ken[i]);
              }
              std :: sort (ken, ken + n);
              std :: sort (naomi, naomi + n);

              f = fairgame(ken, naomi, n);
              //printf("%d", f);

              std :: reverse(ken, ken + n);
              std :: reverse(naomi, naomi + n);

              c = cheating(ken, naomi, n);
              //printf("%d", c);
              printf("Case #%d: %d %d\n",z,c,f);
    }
    return 0;
}


