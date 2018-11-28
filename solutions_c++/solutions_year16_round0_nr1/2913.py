#include <bits/stdc++.h>
using namespace std;
int t,n;
bool a[15];
int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d",&t);
    for (int i=0;i<t;i++) {
        scanf("%d",&n);
        int cnt=0;
        memset (a,false,sizeof a);
        for (int j=1;j<=1000;j++) {
            int k=n*j;
            while (k) {
                if (!a[k%10]) {
                    a[k%10]=true;
                    cnt++;
                }
                k/=10;
            }
            if (cnt>=10) {
                printf("Case #%d: %d\n",i+1,n*j);
                break;
            }
            if (j==100) printf("Case #%d: INSOMNIA\n",i+1);
        }
    }
    return 0;
}

