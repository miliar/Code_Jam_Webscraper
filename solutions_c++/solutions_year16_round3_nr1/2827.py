#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("A-large (3).in" , "r" , stdin);
    freopen("out.txt" , "w" , stdout);
    int t , n;
    int p[26];
    int sum;
    int i1 , i2 , i3;
    scanf("%d" , &t);
    for(int c = 1; c <= t; c++){
        scanf("%d" , &n);
        sum = 0;
        for(int c1 = 0; c1 < n; c1 ++){
            scanf("%d" , &p[c1]);
            sum += p[c1];
        }
        printf("Case #%d: " , c);
        while(sum > 0){
            i1 = 0;
            i2 = 0;
            i3 = 0;
            for(int i = 1; i < n; i ++){
                if(p[i] != 0 && p[i] > p[i1]){
                    i1 = i;
                }
            }
            if(i2 == i1){
                i2 = i1 + 1;
                if(i2 == n){
                    i2 -= 2;
                }
            }
            for(int i = 1; i < n; i ++){
                if(p[i] != 0 && p[i] >= p[i2] && i != i1){
                    i2 = i;
                }
            }
            if(i3 == i1){
                if(i2 == i1 + 1){
                    i3 = i1 + 2;
                    if(i3 == n){
                        i3 -= 3;
                    }
                }
                else{
                    i3 = i1 + 1;
                    if(i3 == n){
                        i3 -= 2;
                    }
                }
            }
            for(int i = 1; i < n; i ++){
                if(p[i] != 0 && p[i] >= p[i3] && i != i1 && i != i2){
                    i3 = i;
                }
            }
            if(p[i1] - p[i2] >= 1){
                if(p[i1] > 1 && 2 * (p[i1] - 2) <= (sum - 2) && 2 * (p[i2]) <= (sum - 2) && (n <= 2 || 2 * (p[i3]) <= (sum - 2))){
                    p[i1] -= 2;
                    sum -= 2;
                    printf("%c%c " , 'A' + i1 , 'A' + i1);
                }
                else{
                    p[i1] -= 1;
                    sum -= 1;
                    printf("%c " , 'A' + i1);
                }
            }
            else{
                if(p[i1] >= 1 && 2 * (p[i1] - 1) <= (sum - 2) && (n <= 2 || 2 * (p[i3]) <= (sum - 2))){
                    p[i1] -= 1;
                    p[i2] -= 1;
                    sum -= 2;
                    printf("%c%c " , 'A' + i1 , 'A' + i2);
                }
                else{
                    p[i1] -= 1;
                    sum -= 1;
                    printf("%c " , 'A' + i1);
                }
            }
            if(sum == 0){
                printf("\n");
            }
        }
    }
    return 0;
}
