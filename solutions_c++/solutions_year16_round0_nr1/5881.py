#include <bits/stdc++.h>
using namespace std;

int a[1000000 + 1];

int main (){
    int n;
    scanf("%d", &n);

    for (int i = 0; i < n; i++){
        scanf("%d", &a[i]);
    }

    for (int i = 0; i < n; i++){
        int temp = a[i];
        int b[10] = {0};
        int cnt = 0;
        int x = 1;
        int times = 0;

        if (temp == 0)
            printf("Case #%d: INSOMNIA\n", i + 1);
        else{
            long long int N, ans;
            ans = temp;
            while(1){
                N = temp * x;
                while(1){
                    int y = N % 10;
                    N /= 10;
                    if (b[y] == 0){
                        b[y]++;
                        cnt++;
                    }
                    if (N == 0 || cnt == 10)
                        break;
                }

                if (cnt == 10)
                    break;
                times++;
                x++;

            }
            printf("Case #%d: %lld\n", i + 1, ans * x);
        }


    }

    return 0;
}
