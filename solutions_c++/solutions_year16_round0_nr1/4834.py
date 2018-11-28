#include <bits/stdc++.h>
using namespace std;

int T;


int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &T);
    for (int cas = 1; cas<=T; cas++){
        printf("Case #%d: ", cas);
        bool seen[10] = {0};
        int N;
        scanf("%d", &N);
        if (N == 0){
            printf("INSOMNIA\n");
            continue;
        }
        int x = 0;
        while(x < 2000000000){
            x += N;
            int t = x;
            while (t > 0){
                seen[t%10] = true;
                t/=10;
            }
            bool done = true;
            for(int i = 0; i<10; i++){
                if (!seen[i]) done = false;
            }
            if (done) break;
        }
        printf("%d\n", x);




    }


}
