#include <stdio.h>
#include <iostream>
using namespace std;

int T,n;
int a[27];
int ans[1010];
int main() {
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
    int C = 1;
    while(T --) {
        scanf("%d",&n);
        int sum = 0;
        for (int i = 0;i < n;i ++) {
            scanf("%d",&a[i]);
            sum += a[i];
        }
        int len = 0;
        while(1) {
            if(len >= sum) break;
            for (int i = 0;i < n;i ++) {
                if(a[i] > 0) {
                    ans[len ++] = i;
                    a[i] --;
                }
            }
        }
        printf("Case #%d:",C ++);

        if(len % 2 == 1) {
            printf(" %c",char('A' + ans[len - 1]));
            len --;
        }
      //  cout <<"len" << len << endl;
        for (int i = len - 1;i >= 1; i -=2) {
            printf(" %c%c",char('A' + ans[i]),char('A' + ans[i - 1]));
        }
        puts("");
    }
}

