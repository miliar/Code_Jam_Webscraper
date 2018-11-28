#include <cstdio>
#include <algorithm>
using namespace std;
int T,S;
int shyness[1010];
int s[1010];
int main(){
    scanf("%d", &T);
    for(int i=1;i<=T;i++){
        scanf("%d", &S);
        char shy;
        scanf("%c",&shy);
        for(int i = 0; i <= S; i++){
            scanf("%c", &shy);
            shyness[i] = shy - '0';
        }
        int ans = 0;
        s[0] = shyness[0];
        for(int i = 1; i <= S; i++){
            s[i] = s[i-1] + shyness[i];
            ans = max(ans, i-s[i-1]);
        }
        printf("Case #%d: %d\n", i, ans);
    }
}

