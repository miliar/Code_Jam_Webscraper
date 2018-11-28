#include<iostream>
#include<cmath>
#include<map>
#include<cstring>
#include<cstdio>
using namespace std;
typedef long long LL;
int a[5][5], b[5][5];

int main(){
    freopen("A-small-attempt2.in", "r", stdin);
    freopen("output1.txt", "w", stdout);
    int T, cases = 1;
    scanf("%d", &T);
    while(T--){
        int x, y;
        scanf("%d", &x);
        int flag = 0, num;
        for(int i = 1; i <= 4; ++i){
            for(int j = 1; j <= 4; ++j)
                scanf("%d", &a[i][j]);
        }
        scanf("%d", &y);
        for(int i = 1; i <= 4; ++i){
            for(int j = 1; j <= 4; ++j)
                scanf("%d", &b[i][j]);
        }
        for(int i = 1; i <= 4; ++i){
            for(int j = 1; j <= 4; ++j){
                if(a[x][i] == b[y][j]){
                    ++flag;
                    num = a[x][i];
                }
            }
        }
        printf("Case #%d: ", cases++);
        if(flag == 1){
            printf("%d", num);
        }
        else if(flag > 1){
            printf("Bad magician!");
        }
        else printf("Volunteer cheated!");
        printf("\n");
    }
    return 0;
}

