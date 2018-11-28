#include <cstdio>
#include <iostream>
#include <cmath>
#include <string>
#include <cstring>
#include <cctype>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#define For(i,N) for(int i=0; i<N; i++)
#define FOR(i,j,k) for(int i=j; i<k; i++)
#define pb push_back
#define mp make_pair
#define ff first
#define ss second

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

bool is_valid_rec(vector<vector<bool> > &WM, vector<bool> &W, vector<bool> &M){
    int workers = 0;
    for (int w=0; w<W.size(); w++)if (W[w]){
        workers++;

        int machines = 0;
        for(int m=0; m<M.size(); m++) if (M[m] && WM[w][m]){
            machines++;
            M[m] = 0;
            W[w] = 0;
            if (!is_valid_rec(WM, W, M))
                return false;
            M[m] = 1;
            W[w] = 1;
        }
        if (machines == 0) return false;
    }

    if (workers == 0){
        int machines = 0;
        for(int m=0; m<M.size(); m++) machines += M[m];
        if (machines != 0) return false;  
    } 
    return true;
}

bool is_valid(int conf, int n){
    vector< vector <bool> > WM(n, vector<bool> (n, 0));
    for (int w=0; w<n; w++) for(int m=0; m<n; m++)
        WM[w][m] = bool(conf & (1 << (w*n + m)));

    vector<bool> W(n, 1), M(n, 1);

    return is_valid_rec(WM, W, M);
}

int read_input(int n){
    int res = 0;
    for (int w=0; w<n; w++) for(int m=0; m<n; m++){
        char c;
        scanf(" %c", &c);
        if (c == '1')
            res |= (1 << (w*n + m));
    }
    return res;
}

void write_conf(int conf, int n){
    for (int w=0; w<n; w++){
        for(int m=0; m<n; m++) printf("%d", int(bool(conf & (1 << (w*n + m)))));
        printf("\n");
    }
    printf("\n");
}

int dist(int inp, int conf){
    int res = 0;
    for(int i=0; i<20; i++){
        if (bool(inp & (1<<i)) && !bool(conf & (1<<i)))
            return 1000;
        if (!bool(inp & (1<<i)) && bool(conf & (1<<i)))
            res++;
    }
    return res;
}

void solve(){
    int n;
    scanf("%d", &n);

    int inp = read_input(n);
    int mindist = n*n;

    for (int conf=0; conf<(1<<(n*n)); conf++){
        if (is_valid(conf, n)){
            //write_conf(conf, n);
            mindist = min(mindist, dist(inp, conf));
        }
    }

    printf("%d\n", mindist);
}

int main(){
  int T;
  scanf(" %d", &T);
  For(t,T){
    printf("Case #%d: ",t+1);
    solve();
  }
  return 0;
}