#include <bits/stdc++.h>

using namespace std;

const int maxN = 10;
const int mod = 1e9 + 7;
char tab[maxN][maxN] , temporal[maxN][maxN];
int p[maxN] , n;
bool ok;

bool used[maxN];
void solve(int pos){
    if(pos == n){
        return;
    }

    int current = p[pos];
    bool entro = false;
    for(int i = 0; i < n; ++i){
        if(!used[i] && temporal[current][i] == '1'){
            used[i] = true;
            solve(pos+1);
            used[i] = false;
            entro = true;
        }
    }
    if(!entro){
        ok = false;
    }
}

int main(){
    freopen("D-small-attempt0.in","r",stdin);
    freopen("on.c","w",stdout);

    int tc;
    cin >> tc;
    for(int number_case = 1; number_case <= tc; ++number_case){
            cin >> n;
            for(int i = 0; i < n; ++i){
                cin >> tab[i];
            }

            int len = n * n;
            int answer = 1e9;
            for(int mask = 0; mask < 1<<len; mask++){
                    int val = 0;
                    ok = true;
                    for(int i = 0; i < len; ++i){
                     int x = i / n , y = i % n;
                        if(mask & (1<<i)){
                                if(tab[x][y] == '0'){
                                        val++;
                                }
                        }else{
                            if(tab[x][y] == '1'){
                                ok = false;
                            }
                        }
                    }

                    if(!ok){
                        continue;
                    }


                    for(int i = 0; i < len; ++i){
                     int x = i / n , y = i % n;
                        if(mask & (1<<i)){
                         temporal[x][y] = '1';
                        }else{
                            temporal[x][y] = '0';
                        }
                    }

                    for(int i = 0; i < n; ++i){
                        p[i] = i;
                    }
                    do{
                            for(int i = 0; i < n; ++i){
                                used[i] = false;
                            }
                            solve(0);

                    }while(next_permutation(p,p+n));

                if(ok){
                    answer = min(answer , val);
                }

            }



            printf("Case #%d: %d\n",number_case, answer);


    }



    return 0;
}
