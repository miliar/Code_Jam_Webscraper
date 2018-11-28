#include <bits/stdc++.h>
using namespace std;

int main (){
    int n;
    scanf("%d", &n);

    for (int k = 0; k < n; k++){
        char a[1000];
        scanf("%s", a);

        int l = strlen(a);
        int cnt = 0;
        for (int i = l - 1; i >= 0; i--){
            if (a[i] == '-'){
                for (int j = i - 1; j >= 0; j--){
                    if (a[j] == '+')
                        a[j] = '-';
                    else if (a[j] == '-')
                        a[j] = '+';
                }
                cnt++;
            }
        }

        printf("Case #%d: %d\n", k + 1, cnt);
    }

    return 0;
}
