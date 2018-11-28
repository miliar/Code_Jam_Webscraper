#include <bits/stdc++.h>

using namespace std;

int N,J;
int b[40];
int cnt = 0;
long long val[12];
vector <int> p;
map <int,bool> primeMap;
int eocnt[2];

void clearmem(){
    cnt = 0;
}

void genB(int lvl){
    if (cnt>=J){
        exit(0);
    }
    if (lvl>=N-1){
        eocnt[0] = eocnt[1] = 0;
        for (int i=1;i<N-1;i++){
            eocnt[i%2] += b[i];
        }
        if (eocnt[0] != eocnt[1]) return;
        for (int i=0;i<N;i++){
            printf ("%d",b[i]);
        }
        for (int i=2;i<=10;i++){
            printf (" %d",i+1);
        }
        cnt++;
        printf ("\n");
        return;
    }
    for (int i=0;i<=1;i++){
        b[lvl] = i;
        genB(lvl+1);
    }
}

void solve(){
    clearmem();
    scanf ("%d%d",&N,&J);
    b[0] = b[N-1] = 1;
    genB(1);
}

int main(){
    freopen ("C-large.in","r",stdin);
    freopen ("Clarge.out","w",stdout);

    int TC;
    scanf ("%d",&TC);
    for (int tc=1;tc<=TC;tc++){
        printf ("Case #%d:\n",tc);
        solve();
    }
return 0;
}
