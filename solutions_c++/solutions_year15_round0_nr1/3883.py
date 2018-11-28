#include <algorithm>
#include <iostream>
#include <cstdio>

using namespace std;

#define MAX 1005

int main(){
    #ifndef ONLINE_JUDGE
     freopen("A-large.in","r",stdin);
     freopen("A-large.out","w",stdout);
    #endif // ONLINE_JUDGE
   char a[MAX];
   int T;
   scanf("%d",&T);
    for(int i= 1; i<= T; i++){
        int n;
        cin >> n >> a;
        int sum = a[0] - '0', res = 0;
        for(int j = 1; j <= n; j++){
            if (a[j]-'0' > 0 && j > sum + res) res = j - sum;
            sum += a[j] - '0';
        }
        printf("Case #%d: %d\n", i, res);
    }
    return 0;
}
