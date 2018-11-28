#include <stdio.h>
#include <algorithm>
using namespace std;

const int N = 2000+10;
char s[N];

int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cas = 1 ; cas <= T ; ++cas) {
        int n;
        scanf("%d %s", &n,s);
        int answer = 0;
        int cnt = 0;
        for(int i = 0 ; i <= n ; ++i) {
            if(s[i]-'0' == 0)continue;
            if(cnt < i) {
                answer += i-cnt;
                cnt = i;
            }
            cnt += s[i]-'0';
        }
        printf("Case #%d: %d\n",cas, answer);
    }
}
