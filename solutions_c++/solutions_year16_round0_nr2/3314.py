#include "iostream"
#include "cstring"
#include "cstdio"
using namespace std;
const int N = 110;
char s[N];
int dp[N][2];
int main(void)
{
    int T;
    scanf("%d", &T);
    int g = 0, n;
    while(T--){
        printf("Case #%d: ", ++g);
        scanf("%s", s);
        int len = strlen(s);
        int cov = 0, sum = 0;
        for(int i = len - 1; i >= 0; -- i){
            if(s[i] == '+' && cov == 0){
                continue;
            }else if(s[i] == '-' && cov == 1){
                continue;
            }else{
                sum ++;
                cov = (cov + 1) % 2;
            }
        }
        printf("%d\n", sum);
    }
    return 0;
}