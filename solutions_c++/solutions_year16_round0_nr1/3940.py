#include <bits/stdc++.h>
using namespace std;

int main(){
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);

    int t;
    scanf("%d", &t);
    for(int k = 1; k <= t; k++){
        int n;
        scanf("%d", &n);
        printf("Case #%d: ", k);
        if(n == 0){
            printf("INSOMNIA\n");
        }else{
            int qtd = 0;
            long long cur = 0;
            vector<bool> ok(10, false);
            while(qtd < 10){
                cur += n;
                long long tmp = cur;
                while(tmp > 0){
                    int d = tmp%10;
                    if(!ok[d]){
                        ok[d] = true;
                        qtd++;
                    }
                    tmp /= 10;
                }
            }
            printf("%lld\n", cur);
        }
    }
    return 0;
}
