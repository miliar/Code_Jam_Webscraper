#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

bool done(long long int digits[10]){
    for(int i = 0; i < 10; i++){
        if(digits[i] == 0)
            return false;
    }
    return true;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output", "w", stdout);
    long long int n;
    scanf("%lld", &n);
    long long int times;
    for(long long int i=0; i<n; i++){
        long long int digits[10] = { 0,0,0,0,0,0,0,0,0,0 };
        long long int N;
        scanf("%lld", &N);
        times = 0;
        if(N == 0){
            printf("Case #%lld: INSOMNIA\n", i+1);
        }
        else{
            while(!done(digits)){
                times += N;
                long long int rest = times;
                while(rest > 0){
                    digits[rest%10] = 1;
                    rest/=10;
                }
            }
            printf("Case #%lld: %lld\n", i+1, times);
        }

    }
    return 0;
}
