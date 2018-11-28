#include<cstdio>
#include<cstring>
using namespace std;
char arr[10000];
char tmp[10000];
int main(){
    int TN;
    scanf("%d", &TN);
    for(int casen = 1 ; casen <= TN ; casen++){
        printf("Case #%d: ", casen);
        int n, m;
        scanf("%d %d", &n, &m);
        gets(arr);
        bool flag = false;
        for(int i = 0 ; i < m ; i++) tmp[i] = '1';
        tmp[m] = 0;
        for(int i = 0 ; i<  n ;i++){
            scanf("%s", arr);
            if(strcmp(arr, tmp) == 0) flag = true;
        }
        gets(arr);
        gets(arr);
        if(flag){
            puts("IMPOSSIBLE");
        }else{
            if(m == 1){
                puts("0 ?");
                continue;
            }
            for(int i = 0 ; i < m-1 ; i++){
                putchar('1');
                putchar('0');
            }
            putchar('?');
            for(int i = 0 ; i < m-1 ; i++)
                putchar('1');
            putchar(' ');
            for(int i = 0 ; i < m-1 ; i++)
                putchar('?');
            puts("");
        }
    }
    return 0;
}
