#include<iostream>
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
int T,N,M,n[110],m[110];
char c,a[110][110];

int main() {
    freopen("input.in","r",stdin);
    freopen("out1.out","w",stdout);
    scanf("%d",&T);
    for(int tt=1;tt<=T;++tt) {
        scanf("%d%d",&N,&M);
        int rez = 0;
        bool ok = 1;
        for(int i=0;i<N;++i) {
            n[i] = 0;
        }
        for(int i=0;i<M;++i) {
            m[i] = 0;
        }
        for(int i=0;i<N;++i) {
            scanf("%c",&c);
            for(int j=0;j<M;++j) {
                scanf("%c",&a[i][j]);
                if(a[i][j]!='.') {
                    ++n[i];
                    ++m[j];
                }
            }
        }
        for(int i=0;i<N;++i) {
            int j = 0;
            while(a[i][j] == '.' && j<M) {
                ++j;
            }
            if(j==M) continue;
            if(a[i][j] == '<') {
                if(n[i] ==1 && m[j] ==1) {
                    ok = 0;
                }
                ++rez;
            }
        }
        for(int i=0;i<N;++i) {
            int j = M-1;
            while(a[i][j] == '.' && j>=0) {
                --j;
            }
            if(j==-1) continue;
            if(a[i][j] == '>') {
                if(n[i] ==1 && m[j]==1) {
                    ok = 0;
                }
                ++rez;
            }
        }
        for(int j=0;j<M;++j) {
            int i = 0;
            while(a[i][j] == '.' && i<N) {
                ++i;
            }
            if(i==N) continue;
            if(a[i][j] == '^') {
                 if(m[j] == 1 && n[i] ==1) {
                    ok = 0;
                }
                ++rez;
            }
        }
        for(int j=0;j<M;++j) {
            int i = N-1;
            while(a[i][j] == '.' && i>=0) {
                --i;
            }
            if(i==-1) continue;
            if(a[i][j] == 'v') {
                 if(m[j] == 1 &&n[i] ==1) {
                    ok = 0;
                }
                ++rez;
            }
        }
        printf("Case #%d: ",tt);
        if(ok) {
            printf("%d\n",rez);
        } else {
            printf("IMPOSSIBLE\n");
        }
    }
    return 0;
}
