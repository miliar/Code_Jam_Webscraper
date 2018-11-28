#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,r,n,i,c, ct;
    long long ans, tem;
    bool flag, chk[10];
    scanf("%d", &t);
    for(r = 1; r <= t; r++){
        c = 0;
        memset(chk, false, sizeof(chk));
        flag = false;
        scanf("%d", &n);
        printf("Case #%d: ",r);
        while(n && (n % 10) == 0){
            n /= 10;
            c++;
        }
        if(!n){
            printf("INSOMNIA");
        }
        else{
            if(c)
                chk[0] = true;
            ct = 1;
            while(!flag){
                ans = ct * n;
                tem = ans;
                while(tem){
                    chk[tem % 10] = true;
                    tem /= 10;
                }
                for(i = 0; i < 10; i++){
                    if(!chk[i])
                        break;
                }
                if(i == 10)
                    flag = true;
                ct++;
            }
            for(i = 0 ; i < c; i++)
                ans *= 10;
            printf("%lld", ans);
        }
        printf("\n");
    }
    return 0;
}
