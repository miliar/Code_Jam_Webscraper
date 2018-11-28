#include <iostream>
#include <cstdio>

using namespace std;

char str [17];
int j;
int m;
int formed;

long long power(long long base , int powr){
    if(powr == 0){
        return 1;
    }
    if(powr % 2 == 1){
        return base * power(base , powr - 1);
    }
    long long res = power(base , powr / 2);
    return res * res;
}

void solve(int ind){
    if(formed == j){
        return;
    }
    if(ind == m / 2 - 1){
        printf("%s%s" , str , str);
        for(int counter = 2; counter <= 10; counter ++){
            long long div = power((long long)counter , m / 2) + 1;
            printf(" %I64d" , div);
        }
        printf("\n");
        formed ++;
        return;
    }
    str[ind] = '0';
    solve(ind + 1);
    str[ind] = '1';
    solve(ind + 1);
}

int main()
{
    freopen("C-small-attempt0.in" , "r" , stdin);
    freopen("out.txt" , "w" , stdout);
    int T;
    scanf("%d" , &T);
    for(int counter = 1; counter <= T; counter ++){
        scanf("%d %d" , &m , &j);
        str[0] = '1';
        str[m / 2 - 1] = '1';
        str[m / 2] = '\0';
        formed = 0;
        printf("Case #%d:\n" , counter);
        solve(1);
    }
    return 0;
}
