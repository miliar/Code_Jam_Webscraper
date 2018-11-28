#include <cstdio>
#include <algorithm>
using namespace std;
int main() {
    int tc;
    scanf("%d",&tc);
    for ( int _tc = 1 ; _tc <= tc ; _tc++ ) {
        printf("Case #%d: ",_tc);
        int smax;
        scanf("%d",&smax);
        char s[1111]={};
        scanf("%s",s);
        int len = smax + 1;
        int ans = 0;
        int sum = s[0]-'0';
        for ( int i = 1 ; i < len ; i++ ) {
            if ( s[i] == '0' ) continue;
            if ( sum < i ) {
                ans += i - sum;
                sum += i - sum;
            }
            sum += s[i]-'0';
        }
        printf("%d\n",ans);
    }
    return 0;
}
