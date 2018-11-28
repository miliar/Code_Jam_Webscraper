#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <utility>
#include <math.h>
#include <ctype.h>
using namespace std;

const int NN = 100 + 8;

int a[NN][NN], N, M;
int b[NN*NN], bn = 0;
int c[NN][NN];

bool isOK(int val) {
    memset(c, 0, sizeof(c));
    for(int i=0; i<N; ++i) {
        bool tag = true;
        for(int j=0; j<M; ++j) {
            if(a[i][j] > val) {
                tag = false;
                break;
            }
        }
        if(tag) {
            for(int j=0; j<M; ++j) c[i][j] = true;
        }
    }
    for(int j=0; j<M; ++j) {
        bool tag = true;
        for(int i=0; i<N; ++i) {
            if(a[i][j] > val) {
                tag = false;
                break;
            }
        }
        if(tag) {
            for(int i=0; i<N; ++i) {
                c[i][j] = true;
            }
        }
    }
    for(int i=0; i<N; ++i)
        for(int j=0; j<M; ++j)
            if(a[i][j] == val && !c[i][j])
                return false;
    return true;
}

bool calc() {
    scanf("%d%d", &N, &M);
    bn = 0;
    for(int i=0; i<N; ++i) {
        for(int j=0; j<M; ++j) {
            scanf("%d", a[i] + j);
            b[bn++] = a[i][j];
        }
    }
    sort(b, b+bn);
    bn = unique(b, b+bn) - b;
    for(int i=0; i<bn; ++i) {
        if(!isOK(b[i])) return false;
    }
    return true;
}

int main() {
    int T;
    scanf("%d", &T);
    for(int Ti=1; Ti<=T; ++Ti) {
        printf("Case #%d: %s\n", Ti, calc() ? "YES":"NO");
    }
    return 0;
}

