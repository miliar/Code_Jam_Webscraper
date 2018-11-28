#include <algorithm>
#include <iostream>
#include <cstdio>

using namespace std;

#define MAX 1005

char a[MAX];
int T;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&T);
    for(int iT = 1; iT <= T; iT++){
        int S;
        scanf("%d%s",&S,&a);
        int sum = a[0] - '0', ans = 0;
        for(int i = 1; i <= S; i++){
            if (i > sum + ans) ans = i - sum;
            sum += a[i] - '0';
        }
        printf("Case #%d: %d\n",iT,ans);
    }
    return 0;
}
