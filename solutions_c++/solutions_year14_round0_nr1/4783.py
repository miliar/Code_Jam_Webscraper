#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <map>
using namespace std;

int main(){
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);

    int tt, T;
    int a[5], row1, row2;
    int i, j, k;

    while(EOF != scanf("%d", &T)){
        for(tt = 1; tt <= T; tt++){
            scanf("%d", &row1);
            getchar();
            char buff[80];
            for(i = 1; i <= 4; i++){
                if(i == row1){
                    for(j = 1; j <= 4; j++)
                        scanf("%d", &a[j]);
                    getchar();
                }
                else
                    gets(buff);
            }
            scanf("%d", &row2);
            getchar();
            int flag = 0, number;
            for(i = 1; i <= 4; i++){
                if(i == row2){
                    for(j = 1; j <= 4; j++){
                        scanf("%d", &a[0]);
                        for(k = 1; k <= 4; k++)
                            if(a[0] == a[k]){
                                number = a[0];
                                flag++;
                            }
                    }
                    getchar();
                } else
                    gets(buff);
            }
            printf("Case #%d: ", tt);
            if(0 == flag){
                printf("Volunteer cheated!\n");
            } else if(1 == flag){
                printf("%d\n", number);
            } else{
                printf("Bad magician!\n");
            }
        }
    }
    return 0;
}
