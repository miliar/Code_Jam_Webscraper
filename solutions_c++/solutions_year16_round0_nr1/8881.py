#include <iostream>
#include <cstdio>

using namespace std;

int main() {

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int Loo,Loop;
    long long N;
    cin>>Loop;
    bool A[10];
    for(Loo=1; Loo<=Loop;Loo++)
    {
        scanf("%lld",&N);
        printf("Case #%d: ",Loo);
        if(N==0) {
            printf("INSOMNIA\n");
            continue;
        }
        memset(A,0,sizeof(A));
        long long cnt = 0, x, Cur = 0;

        while(cnt != 10){
            Cur += N;
            x = Cur;
            while(x){
                if(A[x%10] == false)
                    cnt++;
                A[x%10] = true;
                x/=10;
            }
        }

        printf("%lld\n", Cur);
    }
    return 0;



}