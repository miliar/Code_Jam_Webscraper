#include<iostream>
#include<stdio.h>
#include<vector>
#include<string.h>
using namespace std;

int main(){
    long long L, X, i, j, runs, R, C;
    int sign;
    char s[10001];
    char cur;
    pair<char, int> arr[256][256];
    arr['i']['i'] = make_pair('1', 1);
    arr['i']['j'] = make_pair('k', 0);
    arr['i']['k'] = make_pair('j', 1);

    arr['j']['j'] = make_pair('1', 1);
    arr['j']['i'] = make_pair('k', 1);
    arr['j']['k'] = make_pair('i', 0);

    arr['k']['j'] = make_pair('i', 1);
    arr['k']['k'] = make_pair('1', 1);
    arr['k']['i'] = make_pair('j', 0);

    scanf("%lld", &runs);
    for(j=1; j<=runs; j++){
        scanf("%lld %lld %s", &L, &X, s);
        R = 1;
        C=0;
        cur = '1';
        sign = 0;
        while (R <= X){
            //printf("%c_%d ", cur, sign);
            if(cur == '1'){
                cur = s[C];
                C = (C+1)%L;
                if(C == 0)
                    R++;
                continue;
            }
            if(cur == 'i' && sign == 0)
                break;
            //printf("%c * %c ", cur, s[C]);
            sign = (arr[cur][s[C]].second + sign) %2;
            cur = arr[cur][s[C]].first;
            C = (C+1)%L;
            if(C == 0)
                R++;
        }
        if(R>X){
            printf("Case #%d: NO\n", j);
            continue;
        }
        //printf("\n");
        cur = '1';
        while (R <= X){
            //printf("%c_%d ", cur, sign);
            if(cur == '1'){
                cur = s[C];
                C = (C+1)%L;
                if(C == 0)
                    R++;
                continue;
            }
            //printf("%c * %c ", cur, s[C]);
            if(cur == 'j' && sign == 0)
                break;
            sign = (arr[cur][s[C]].second + sign) %2;
            cur = arr[cur][s[C]].first;
            C = (C+1)%L;
            if(C == 0)
                R++;
        }
        if(R>X){
            printf("Case #%d: NO\n", j);
            continue;
        }
        //printf("\n");
        cur = '1';
        while (R <= X){
            //printf("%c_%d ", cur, sign);
            if(cur == '1'){
                cur = s[C];
                C = (C+1)%L;
                if(C == 0)
                    R++;
                continue;
            }
            //printf("%c * %c ", cur, s[C]);
            sign = (arr[cur][s[C]].second + sign) %2;
            cur = arr[cur][s[C]].first;
            C = (C+1)%L;
            if(C == 0)
                R++;
        }

        if(cur=='k' && sign == 0)
            printf("Case #%d: YES\n", j);
        else
            printf("Case #%d: NO\n", j);
    }


    return 0;
}
