#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T, d;
    char str[1005];
    scanf("%d",&T);
    for(int t = 1; t <= T; t++){
        scanf("%d%s",&d,str);
        int sum = str[0] - '0';
        int ans = 0;
        for(int i = 1; i < strlen(str); i++){
            if(i <= sum){
                sum += str[i] - '0';
            }
            else {
                sum ++;
                sum += str[i] - '0';
                ans ++;
            }
        }
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}
