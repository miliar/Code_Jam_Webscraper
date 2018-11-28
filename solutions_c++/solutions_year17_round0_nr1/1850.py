#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;
char str[1001];
int k;
bool flip[2001], flipped[2001];
int main(){
    int TC;
    scanf("%d", &TC);
    for(int tc = 1; tc <= TC; ++tc){
        scanf("%s %d", str, &k);
        int l = strlen(str);
        for(int i = 0; i < l; ++i) flip[i] = flipped[i] = 0;
        if(str[0] == '-') flip[0] = true, flipped[k] = true;
        for(int i = 1; i < l; ++i){
            if((str[i] != str[i-1]) != flipped[i]) flip[i] = true, flipped[k + i] = true;
            else flip[i] = false;
        }
        bool died = false;
        for(int i = l-k+1; i < l; ++i){
            if(flip[i]) died = true;
        }
        if(died) printf("Case #%d: IMPOSSIBLE\n", tc);
        else{
            int ans = 0;
            for(int i = 0; i < l; ++i) ans+= flip[i];
            printf("Case #%d: %d\n", tc, ans);
        }
    }
}
