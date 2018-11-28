#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
using namespace std;

char str[2][20]={"Bad magician!","Volunteer cheated!"};
int num1[4][4],num2[4][4];
int flag;

int main(){
    int T;
    int Case = 0;
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    scanf("%d", &T);
    while(T--){
        int m,n;
        int i,j;
        flag = 0;
        scanf("%d", &m);
        for(i=0; i<4; ++i){
            for(j=0; j<4; ++j){
                scanf("%d", &num1[i][j]);
            }
        }
        scanf("%d", &n);
        for(i=0; i<4; ++i){
            for(j=0; j<4; ++j){
                scanf("%d", &num2[i][j]);
            }
        }

        int ans;
        for(i=0; i<4; ++i){
            for(j=0; j<4; ++j){
                if(num1[m-1][i] == num2[n-1][j]){
                    flag++;
                    ans = num2[n-1][j];
                    break;
                }
            }
        }
        printf("Case #%d: ", ++Case);
        if(flag==1){
            printf("%d\n", ans);
        }
        else if(flag == 0){
            printf("%s\n", str[1]);
        }
        else{
            printf("%s\n", str[0]);
        }
    }
    return 0;
}
