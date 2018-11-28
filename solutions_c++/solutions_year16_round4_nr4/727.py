#include<stdio.h>
#include<iostream>
#include<vector>
#include<map>
#include<string>
#define pb push_back
using namespace std;

string s[30];
int N,T;
int viz[30][30];
bool ok = 1;
int n[30],nn[30];
int L;

void backy(int y) {
    if(y==N) return;
    int x = nn[y];
    bool hey = 0;
    for(int i=0;i<N;++i) {
        if(viz[x][i] && !n[i]) {
            n[i] = 1;
            backy(y+1);
            n[i] = 0;
            hey = 1;
        }
    }
    if(!hey) ok = 0;
}

void backy2(int x) {
    if(x==N) {
        backy(0);
        return;
    }
    for(int i=0;i<N;++i) {
        if(nn[i] == -1) {
            nn[i] = x;
            backy2(x+1);
            nn[i] = -1;
        }
    }
}

int main() {
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    scanf("%d",&T);
    for(int i=0;i<=20;++i) {
        nn[i] = -1;
    }
    for(int t=1;t<=T;++t) {
        printf("Case #%d: ",t);
        scanf("%d",&N);
        int cnt = 0;
        for(int i=0;i<N;++i) {
            cin>>s[i];
            for(int j=0;j<N;++j) {
                if(s[i][j]=='1') ++cnt;
            }
        }
        int ma = N*N-cnt;
        for(int l=0;l<(1<<(N*N));++l) {
            int x = l;
            int k = 0;
            for(int i=0;i<N*N;++i) {
                if(x%2) {
                    viz[i/N][i%N] = 1;
                    if(s[i/N][i%N]=='0') {
                        ++k;
                    } 
                } else {
                    viz[i/N][i%N] = 0;
                    if(s[i/N][i%N] == '1') {
                        viz[i/N][i%N] = 1;
                    }
                }
                x/=2;
            }
            L = l;
            ok = 1;
            backy2(0);
            if(ok) {
                ma = min(ma,k);
            }
        }
        printf("%d\n",ma);
    }
    return 0;
}

