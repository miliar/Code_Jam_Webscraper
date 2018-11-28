#include <cstdio>
#include <cstdlib>

int ar[20], n, k;

void solve(long long n){
    if (n == 0){
        printf("INSOMNIA\n");
        return ;
    }

    int summ = 0;
    for (int i = 0; i < 10; ++i){
        ar[i] = 0;
    }

    long long current_value = 0;

    while (summ < 10){
        current_value += n;
        long long temp = current_value;
        while (temp > 0){
            int current_digit = temp % 10;
            temp = temp / 10;
            summ += 1 - ar[current_digit];
            ar[current_digit] = 1;
        }
    }

    printf("%lld\n", current_value);
}

int main(){

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    scanf("%d", &k);

    for (int i = 0; i < k; ++i){
        scanf("%d", &n);
        printf("Case #%d: ", i+1);
        solve(n);
    }

    return 0;
}
