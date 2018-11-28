#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

const int inf = 1e9+123;
const int N = 10101;

char chs[5] = "1ijk";
char c1[4][5] = {
    "1ijk",
    "i1kj",
    "jk1i",
    "kji1"
};
int cf[4][4] = {
    {1,1,1,1},
    {1,-1,1,-1},
    {1,-1,-1,1},
    {1,1,-1,-1}
};
char mul[256][256],suff[N];
int coef[256][256];
int ssuff[N],n,x;
char s[N];

void solve(){
    scanf(" %d %d %s",&n,&x,s+1);
    for(int i = n + 1; i <= n * x; i++)
        s[i] = s[i - n];
    
    n *= x;
    suff[n + 1] = '1';
    ssuff[n + 1] = 1;
    for(int i = n; i > 0; i--){
        suff[i] = mul[s[i]][suff[i + 1]];
        ssuff[i] = ssuff[i + 1] * coef[s[i]][suff[i + 1]];
    }
    char pref = '1';
    int cpref = 1;
    for(int i = 1; i < n; i++){
        cpref *= coef[pref][s[i]];
        pref = mul[pref][s[i]];
        if(pref != 'i' || cpref != 1)
            continue;
        char middle = '1';
        int cmiddle = 1;
        for(int j = i + 1; j < n; j++){
            cmiddle *= coef[middle][s[j]];
            middle = mul[middle][s[j]];
            if(middle == 'j' && cmiddle == 1){
                if(suff[j + 1] == 'k' && ssuff[j + 1] == 1){
                    printf("YES\n");
                    return;
                }
            }
        }
    }
    printf("NO\n");
}

int main(){
    
    for(int i = 0; i < 4; i++){
        for(int j = 0; j < 4; j++){
            mul[chs[i]][chs[j]] = c1[i][j];
            coef[chs[i]][chs[j]] = cf[i][j];
        }
    }
    
    int asd;
    scanf(" %d",&asd);
    
    for(int i = 1; i <= asd; i++){
        printf("Case #%d: ", i);
        solve();
    }
    
    return 0;
}

