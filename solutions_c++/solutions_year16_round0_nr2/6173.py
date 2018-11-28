#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#define LL long long

using namespace std;

char S[110];
int len;
bool p[110];

void show(){
    for(int i = 1; i <= len; i++){
        printf("%d ", p[i]);
    }
    puts("");
}

void flip(int i){
    int m = 1, n = i;
    for(; m < n; m++, n--){
        bool tmp = p[m];
        p[m] = !p[n];
        p[n] = !tmp;
    }
    if(m == n) p[m] = !p[m];
}


int check(){
    bool flg = true;
    int cost = 0;
    for(int i = 1; i <= len; i++){
        if(flg && !p[i]) flg = false, cost++;
        if(!flg && p[i]) flg = true;
    }
    return cost;
}

int IDA(int cur, int limit){
    int cost = check();
    if(cur + cost > limit) return cost;
    if(!cost) return 0;
    for(int i = 1; i <= len; i++){
        flip(i);
        cost = min(IDA(cur + 1, limit), cost);
        if(!cost) return 0;
        flip(i);
    }
    return cost;
}

int search(void){
    int res, dep = 0;
    for(dep = 0; (res = IDA(0, dep)); dep += res);
    return dep;
}


int main(void){
    int T, kase = 0;
    scanf("%d", &T);
    while(T--){
        scanf("%s", S);
        for(len = 0; S[len]; len++){
            p[len + 1] = (S[len] == '+' ? 1 : 0);
        }
        printf("Case #%d: ", ++kase);
        printf("%d\n", search());
    }

    return 0;
}

