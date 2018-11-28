#include<cstdio>

using namespace std;

int T, N, round, sumnum;
bool num [10] = {false};


void add(){
    int temp = round*N, digit;
    while (temp > 0){
        digit = temp%10;
        if (!num[digit]){
            num[digit] = true;
            sumnum++;
        }
        temp/=10;
    }
}


int main(){
    freopen("large.in", "r", stdin);
    freopen("large.out", "w", stdout);
    scanf("%d\n", &T);
    for (int t = 1; t <= T; ++t){
        scanf("%d", &N);
        if (!N) {
            printf("Case #%d: INSOMNIA\n", t);
            continue;
        }
        round = sumnum = 0;
        for (int i = 0; i < 10; ++i){
            num[i] = false;
        }
        while (sumnum < 10){
            ++round;
            add();
        }
        printf("Case #%d: %d\n", t, round*N);
    }
}
