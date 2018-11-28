#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <string>
#include <iostream>

using namespace std;

#define INF 1000000007

char a[4], b[4];
int menor;
int resA, resB;
string r1, r2;
int n;

void backtrack(int k) {
    if (k==n) {
//        printf("** %s %s\n", a, b);
        int u, v;
        u=atoi(a);
        v=atoi(b);
        if (abs(u-v)<menor) {
            menor=abs(u-v);
            resA=u;
            resB=v;
            r1=a;
            r2=b;
        }
        else {
            if (abs(u-v)==menor) {
                if (u<resA) {
                    menor=abs(u-v);
                    resA=u;
                    resB=v;
                    r1=a;
                    r2=b;
                }
                else {
                    if (u==resA) {
                        if (v<resB) {
                            menor=abs(u-v);
                            resA=u;
                            resB=v;
                            r1=a;
                            r2=b;
                        }
                    }
                }
            }
        }
    }
    else {
        int i, j;
        for (i='0'; i<='9'; i++) {
            for (j='0'; j<='9'; j++) {
                char x, y;
                x=a[k];
                y=b[k];
                if (a[k]=='?') {
                    a[k]=i;
                }
                if (b[k]=='?') {
                    b[k]=j;
                }
                backtrack(k+1);
                a[k]=x;
                b[k]=y;
            }
        }
    }
}

int main() {
//    freopen("B-small-attempt0.in", "r", stdin);
//    freopen("B-small-attempt0.out", "w", stdout);
    int t;
    scanf("%d", &t);
    int teste;
    for (teste=1; teste<=t; teste++) {
        scanf("%s %s", a, b);
        n=strlen(a);
        menor=INF;
        backtrack(0);
        printf("Case #%d: %s %s\n", teste, r1.c_str(), r2.c_str());
    }
    return 0;
}
