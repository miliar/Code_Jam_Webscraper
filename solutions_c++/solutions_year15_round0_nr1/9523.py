#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

const int maxn = 1000+10;

char shy[maxn];

int main(){
    int t, s, flag;
    freopen("input.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &t);
    flag = 1;
    while (t--) {
        memset(shy, 0, sizeof(shy));
        scanf("%d %s", &s, shy);
        int cnt, num;
        cnt = num = 0;
        for (int i = 0; i <= s; i ++) {
            if (num < i) {
              //  cout << i << endl;
                cnt += i-num;
                num += i-num;
              //  cout << cnt << endl;
            }
            num += (shy[i]-'0');
        }
        printf("Case #%d: %d\n", flag++, cnt);
    }
    return 0;
}
