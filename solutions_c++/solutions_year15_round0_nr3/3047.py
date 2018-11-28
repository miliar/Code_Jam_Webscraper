#include<cstdio>
#include<cstring>
using namespace std;
const int MAX = 10000 + 10;
char arr[MAX];
int rec[MAX];
int XD[5][5] = { {0, 0, 0, 0, 0},
                 {0, 1, 2, 3, 4},
                 {0, 2, -1, 4, -3},
                 {0, 3, -4, -1, 2},
                 {0, 4, 3, -2, -1}};
int main(){
    freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);
    int TN;
    scanf("%d", &TN);
    for(int casen = 1 ; casen <= TN ; casen++){
        memset(arr, 0, sizeof(arr));
        int n, m;
        bool flag1 = false, flag2 = false;
        scanf("%d %d %s", &n, &m, arr);
        for(int i = 0 ; i  < n ; i++){
            rec[i] = arr[i] - 'i' + 2;
        }
        for(int i = 1 ; i < m ; i++){
            for(int j = n * i ; j < n * (i+1) ; j++){
                rec[j] = rec[j % n];
            }
        }
        n *= m;
        int tmp = 1;
        for(int i = 0 ; i < n ; i++){
            bool fu = false;
            if(tmp < 0) fu = true, tmp *= -1;
            tmp = XD[tmp][rec[i]];
            if(fu) tmp *= -1;
            if(!flag1){
                if(tmp == 2) flag1 = true;
            }else if(!flag2){
                if(tmp == 4) flag2 = true;
            }
        }
        printf("Case #%d: ", casen);
        if(flag1 && flag2 && tmp == -1) puts("YES");
        else puts("NO");
    }
    return 0;
}
