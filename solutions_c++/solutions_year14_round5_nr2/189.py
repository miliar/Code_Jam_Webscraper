//Fruit of Light
//FoL CC
//Apple Strawberry

#include<cstdio>
#include<algorithm>
#include<vector>
#include<iostream>
#include<set>
#include<map>
#include<queue>
#include<cmath>
#include<cstring>

using namespace std;

#define For(i, n) for(int i = 0; i<(n); ++i)
#define ForEach(it, i) for(typeof i.begin() it = i.begin(); it!=i.end(); ++it)
#define MLINF -823456789
#define eps 1e-9

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

int n,p,q;
int can[30][1000];
#define OFF 12

int extra(){
    scanf("%d%d%d",&p, &q, &n);
    For(i, 30) For(j, 500) can[i][j] = 0;
    For(s, 30)
        for(int i = 0; i*q<=202; ++i){
            for(int j = i*q+1; j<=i*q+max(0,i+s-OFF)*p && j<=202; ++j)
                can[s][j] = 1;
    }
    ll score[2][3000];
    For(k, 2) For(i, 3000) score[k][i] = MLINF;
    score[0][1] = 0;

    int h,g;
    For(k, n){
        For(i, 3000) score[(k+1)%2][i] = MLINF;
        scanf("%d%d",&h,&g);
        int potrebujem = 0;
        while(!can[potrebujem][h]) potrebujem++;
        potrebujem -= OFF;
        int ziskam = (h-1)/q + 1;
        //printf("%d %d %d %d\n", potrebujem, ziskam,h, g);
        // zautocim
        For(i, 2100) if (i+potrebujem>=0) score[(k+1)%2][i] = max(score[(k+1)%2][i], score[k%2][i+potrebujem]+g);
        // nezautocim
        For(i, 2100) score[(k+1)%2][i+ziskam] = max(score[(k+1)%2][i+ziskam], score[k%2][i]);
        // pass 
        For(i, 2500) score[(k+1)%2][2500-i-1] = max(score[(k+1)%2][2500-i-1], score[(k+1)%2][2500-i]);
        //For(i, 10) printf("%lld ", score[(k+1)%2][i]);
        //printf("\n");
    }
    printf("%lld\n", score[n%2][0]);
}

int main(){
    int T;
    scanf("%d",&T);
    For(i,T){
        printf("Case #%d: ",i+1);
        extra();
    }
}
