#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <stack>
using namespace std;

#define For(i,n) for(int i=0; i<(n); i++)
#define mp(a,b) make_pair((a),(b))
typedef long long ll;
typedef pair<int,int> pii;

char A[147][147];

void solve() {
    int r,s;
    scanf("%d %d",&r,&s);
    For(i,r) For(j,s) scanf(" %c",&A[i][j]);
    int res=0;
    int P1[147],P2[147];
    For(i,142) P1[i]=P2[i]=0;
    For(i,r) {
        int p=0;
        For(j,s) if(A[i][j]!='.') p++;
        P1[i]=p;
    }
    For(j,s) {
        int p=0;
        For(i,r) if(A[i][j]!='.') p++;
        P2[j]=p;
    }
    For(i,r) For(j,s) {
        if(A[i][j]!='.' && P1[i]==1 && P2[j]==1) {printf("IMPOSSIBLE\n"); return;}
    }
    For(i,r) {
        For(j,s) {
            if(A[i][j]!='.') {
                if(A[i][j]=='<') res++;
                break;
            }
        }
        for(int j=s-1; j>=0; j--) {
            if(A[i][j]!='.') {
                if(A[i][j]=='>') res++;
                break;
            }
        }
    }
    For(j,s) {
        For(i,r) {
            if(A[i][j]!='.') {
                if(A[i][j]=='^') res++;
                break;
            }
        }
        for(int i=r-1; i>=0; i--) {
            if(A[i][j]!='.') {
                if(A[i][j]=='v') res++;
                break;
            }
        }
    }
    printf("%d\n",res);
}

int main() {
    int t;
    scanf("%d",&t);
    For(i,t) {
        printf("Case #%d: ",i+1);
        solve();
    }
}
