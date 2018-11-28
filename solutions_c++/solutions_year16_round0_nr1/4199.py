#include <iostream>

bool check(int *);

using namespace std;

void citoa(int num, char *pStr){
    int radix = 10;
    int deg = 1;
    int cnt = 0;
    int i;

    if(pStr == NULL) return;

    if(num < 0){
        *pStr = '-';
        num *= -1;
        pStr++;
    }

    while(1){
        if( (num / deg) > 0)
            cnt++;
        else
            break;

        deg *= radix;
    }
    deg /= radix;

    for(i = 0; i < cnt; i++, pStr++){
        *pStr    = (num / deg) + '0';
        num        -= (num / deg) * deg;
        deg        /= radix;
    }
    *pStr = '\0';
}



int main() {
    int n;
    scanf("%d", &n);

    for(int i=0; i<n; i++){
        int number;
        int table[10] = {0, };
        scanf("%d", &number);

        if(number == 0){
            printf("Case #%d: INSOMNIA\n", i+1);
            continue;
        }
        int k=1;
        int t = number;
        while(true){
            char tmp[65] = {0,};
            citoa(t, tmp);
            for(int k=0; k<strlen(tmp); k++){
                table[tmp[k] - '0'] = 1;
            }

            bool result = check(table);
            if(result == true)
                break;
            t = number * k++;
        }
        printf("Case #%d: %d\n", i+1, t);
    }
    return 0;
}

bool check(int *tmp) {
    for(int i=0; i<10; i++){
        if(tmp[i] == 0)
            return false;
    }
    return true;
}