#include<stdio.h>
#include<map>
#include<queue>
#include<string>
#include<stdlib.h>
#include<iostream>
#include<string.h>
#include<vector>
#include<algorithm>
using namespace std;
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)
#define FOE(i,s,e) for(int i=(s);i<=(int)(e);i++)
#define CLR(s) memset(s,0,sizeof(s))
typedef long long LL;
#define PB push_back

int n,m;
int a[200][200];
bool cut[200][200];

int main(){
    int ca; scanf("%d",&ca);
    FOE(tt,1,ca){
        scanf("%d%d",&n,&m);
        bool ans=true;
        FOR(i,0,n) FOR(j,0,m) scanf("%d",&a[i][j]);

        for (int h=100; h>0 && ans; h--){
            CLR(cut);
            FOR(i,0,n){
                bool ok=true;
                FOR(j,0,m){
                    if (a[i][j] > h) ok=false;
                }
                if (ok) FOR(j,0,m) cut[i][j]=true;
            }
            FOR(j,0,m){
                bool ok=true;
                FOR(i,0,n){
                    if (a[i][j] > h) ok=false;
                }
                if (ok) FOR(i,0,n) cut[i][j]=true;
            }
            FOR(i,0,n) FOR(j,0,m) if (!cut[i][j] && a[i][j]==h) ans=false;
        }
        printf("Case #%d: %s\n", tt, ans?"YES":"NO");

    }
    return 0;
}
