#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;


int N, n, tag, num, q1, q2, ans;
int a[4][4], b[4][4];

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A.out", "w", stdout);
    while(scanf("%d", &N) != EOF){
        for(int n = 1;n <= N;n++){
            num = 0;
            scanf("%d", &q1);
            for(int i = 0;i < 4;i++){
                for(int j = 0;j < 4;j++){
                    scanf("%d", &a[i][j]);
                }
            }
            scanf("%d", &q2);
            for(int i = 0;i < 4;i++){
                for(int j = 0;j < 4;j++){
                    scanf("%d", &b[i][j]);
                }
            }
            for(int i = 0;i < 4;i++){
                tag = 0;
                for(int j = 0;j < 4;j++){
                    if(b[q2-1][j] == a[q1-1][i]){
                        tag = 1;
                        ans = b[q2-1][j];
                        break;
                    }
                }
                if(1 == tag){
                    num++;
                }
            }
            if(num == 0){
                printf("Case #%d: Volunteer cheated!\n", n);
            }
            else if(num == 1){
                printf("Case #%d: %d\n", n, ans);
            }
            else{
                printf("Case #%d: Bad magician!\n", n);
            }
        }
    }
    return 0;
}
