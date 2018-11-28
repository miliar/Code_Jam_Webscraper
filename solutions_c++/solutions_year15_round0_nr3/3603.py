#include <algorithm>
#include <iostream>
#include <cstring>

const int inf = 1e9 + 143;

const int maxn = 10101;

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

char mul[256][256];
int coef[256][256];

char suf[maxn];
int csuf[maxn];
char s[maxn];

void solve(){
    int a, b;
    
    scanf(" %d %d",&a,&b);
    scanf(" %s",s+1);
    
    for(int i = a+1; i <= a*b; i++){
        s[i] = s[i-a];
    }
    
    a *= b;
    
    suf[a+1] = '1';
    csuf[a+1] = 1;
    for(int i = a; i > 0; i--){
        suf[i] = mul[s[i]][suf[i+1]];
        csuf[i] = csuf[i+1] * coef[s[i]][suf[i+1]];
    }
    char pref = '1';
    int cpref = 1;
    for(int i = 1; i < a; i++) {
        cpref *= coef[pref][s[i]];
        pref = mul[pref][s[i]];
        
        if(pref != 'i' || cpref != 1)
            continue;
        
        char m = '1';
        int mid = 1;
        
        for(int j = i+1; j < a; j++) {
            
            mid *= coef[m][s[j]];
            m = mul[m][s[j]];
            
            
            if(m == 'j' && mid == 1){
                if(suf[j+1] == 'k' && csuf[j+1] == 1){
                    printf("YES\n");
                    return;
                }
            }
        }
    }
    printf("NO\n");
}

int main(){
    
#ifdef KAZAR
    freopen("f.input","r",stdin);
    freopen("f.output","w",stdout);
    freopen("error","w",stderr);
#endif
    
    for(int i = 0; i < 4; i++){
        for(int j = 0; j < 4; j++){
            mul[chs[i]][chs[j]] = c1[i][j];
            coef[chs[i]][chs[j]] = cf[i][j];
        }
    }
    
    int a;
    scanf("%d",&a);
    
    for(int i = 1; i <= a; i++){
        printf("Case #%d: ", i);
        solve();
    }
    
    return 0;
}

