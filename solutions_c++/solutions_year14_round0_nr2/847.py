#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <string>
#include <iostream>
#define MAXX 100010

using namespace std;

double inicio[MAXX];
double vel[MAXX];
double tempo[MAXX];

int main() {
//    freopen("B-large.in", "r", stdin);
//    freopen("cookie_clicker_alpha_saida.txt", "w", stdout);
    int t, teste;
    scanf("%d", &t);
    for (teste=1; teste<=t; teste++) {
        double c, f, x;
        scanf("%lf %lf %lf", &c, &f, &x);
        inicio[0]=0;
        vel[0]=2;
        tempo[0]=inicio[0]+x/vel[0];
        int i;
        for (i=1; i<=x; i++) {
            inicio[i]=inicio[i-1]+c/vel[i-1];
            vel[i]=vel[i-1]+f;
            tempo[i]=inicio[i]+x/vel[i];
        }
        double menor=-1;
        for (i=0; i<=x; i++) {
            if (menor==-1 || tempo[i]<menor) {
                menor=tempo[i];
            }
        }
        printf("Case #%d: %.7lf\n", teste, menor);
    }
    return 0;
}































