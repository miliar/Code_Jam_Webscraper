#include<iostream>
#include<cstdio>
#include<cmath>

using namespace std;

int n, k;
int init[100], open[100], nk[100];
int key[100][100];
int ok[1100000];
int have[1100000][25];
int map[300];


int ok1(int s) {
    if (s == (1<<n) - 1) {
        ok[s] = 1;
        return 1;
    }
    
    if (ok[s] != 0) return ok[s];
    
    ok[s] = -1;

    for(int i=0; i<=n; i++) have[s][i] = 0;
    
    for(int i=0; i<k; i++)
        have[s][init[i]] ++;
    for(int i=0; i<n; i++)
        if (((s>>i) & 1) != 0){
            for(int j=0; j<nk[i]; j++) 
                have[s][key[i][j]] ++;
            have[s][open[i]] --;
        }                        
    
    for(int i=0; i<n; i++)
        if ((((s >> i) & 1) == 0) && have[s][open[i]] > 0) 
            if (ok1(s | (1<<i)) == 1) {
                ok[s] = 1;
                break;
            }
    
    return ok[s];
}

void trace(int s) {
    if (s == (1<<n)-1) return;
    for(int i=0; i<n; i++)
        if (((s >> i) & 1) == 0 && have[s][open[i]] > 0) 
            if (ok[s | (1<<i)] == 1) {
                cout << i+1 << " ";
                trace(s | (1<<i));
            }
}

int main() {
    int ntest;
    freopen("d.in", "r", stdin);
    freopen("d.txt", "w", stdout);
    scanf("%d", &ntest);
    
    for(int test=0; test<ntest; test++) {
        cout << "Case #" << test+1 << ": ";
        scanf("%d%d", &k, &n);
        /* Initialization */
        for(int i=0; i < (1<<n); i++) ok[i] = 0;
        for(int i=0; i<=200; i++) map[i] = 0;
        /**/
                
        for(int i=0; i<k; i++) {  
            scanf("%d", &init[i]);
            map[init[i]]=1;
        }
            
        for(int i=0; i<n; i++) {
            scanf("%d%d", &open[i], &nk[i]);
            map[open[i]] = 1;
            for(int j=0; j<nk[i]; j++) {
                scanf("%d", &key[i][j]);
                map[key[i][j]] = 1;
            }
        }
        
       // if (test == 10) cout << k << " " << n << open[1] << " " << open[1] <<endl;
        
        for(int i=1; i<=200; i++)
            map[i] += map[i-1];
            
        for(int i=0; i<k; i++)
            init[i] = map[init[i]];
        for(int i=0; i<n; i++) {
            open[i] = map[open[i]];
            for(int j=0; j<nk[i]; j++)
                key[i][j] = map[key[i][j]];
        }
        
        if (ok1(0) == 1) {
            trace(0);
        }
        else 
            cout << "IMPOSSIBLE";
        cout << endl;
    }
    
    return 0;
}
