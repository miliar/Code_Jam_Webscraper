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

int n;
char A[5][5];

vector<bool> T;

bool fakt(vector<int> P, int k) {
    if(k==n) return true;
    bool moze=false;
    int kto=P[k];
    For(i,n) if(A[kto][i]=='1' && T[i]) moze=true;
    if(!moze) return false;
    For(i,n) if(A[kto][i]=='1' && T[i]) {
        T[i]=false;
        if(!fakt(P,k+1)) return false;
        T[i]=true;
    }
    return true;
}

bool over() {
    vector<int> P; For(i,n) P.push_back(i);
    do{
        T.clear();
        T.resize(n,true);
        if(!fakt(P,0)) return false;
    } while(next_permutation(P.begin(),P.end()));
    return true;
}

void solve(int por) {
    scanf(" %d",&n);
    For(i,n) For(j,n) scanf(" %c",&A[i][j]);
    int res=1000;
    For(i,1<<(n*n)) {
        int poc=0; bool t=true;
        For(j,n*n) if(i&(1<<j)) {
            poc++;
            if(A[j/n][j%n]=='1') t=false;
        }
        if(!t) continue;
        For(j,n*n)
            if(i&(1<<j)) {
                A[j/n][j%n]='1';
            }
        if(over()) {
            res=min(res,poc);
            //printf("@%d\n",poc);
            //For(p1,n) {For(p2,n) printf("%c",A[p1][p2]); printf("\n");}
        }
        For(j,n*n)
            if(i&(1<<j)) {
                A[j/n][j%n]='0';
            }
    }
    printf("Case #%d: %d\n",por,res);
}

int main() {
    int t;
    scanf("%d",&t);
    For(i,t) solve(i+1);
}
