#include <bits/stdc++.h>
using namespace std;

long long pot[15][35];

void pre(){
    for(int i = 2; i <= 10; i++){
        pot[i][0] = 1;
        for(int j = 1; j < 32; j++){
            pot[i][j] = pot[i][j - 1]*1LL*i;
        }
    }
}

int divisor(long long n){
    int sqn = sqrt(n);
    for(int i = 2; i <= sqn; i++){
        if(n%i == 0){
            return i;
        }
    }
    return -1;
}

vector<int> jamcoin(int n, int num[]){
    vector<int> ret;
    for(int i = 2; i <= 10; i++){
        long long val = 0;
        for(int j = 0; j < n; j++){
            if(num[j]) val += pot[i][j];
        }
        int d = divisor(val);
        if(d == -1){
            ret.clear();
            break;
        }
        ret.push_back(d);
    }
    return ret;
}

int main(){
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);

    pre();

    int t;
    scanf("%d", &t);
    for(int k = 1, n, j; k <= t; k++){
        scanf("%d %d", &n, &j);
        printf("Case #%d:\n", k);
        int cur[n + 5];
        cur[0] = 1;
        for(int i = 1; i < n - 1; i++){
            cur[i] = 0;
        }
        cur[n - 1] = 1;
        while(j){
            vector<int> go = jamcoin(n, cur);
            if(!go.empty()){
                for(int i = n - 1; i >= 0; i--){
                    printf("%d", cur[i]);
                }
                assert(go.size() == 9);
                for(int i = 0; i < 9; i++){
                    printf(" %d", go[i]);
                }
                printf("\n");
                j--;
            }
            do{
                // Adding 1 to cur
                for(int i = 0; i < n; i++){
                    if(cur[i] == 0){
                        cur[i] = 1;
                        break;
                    }
                    cur[i] = 0;
                }
                assert(cur[n - 1]);
            }while(!cur[0] || !cur[n - 1]);
        }
    }
    return 0;
}
