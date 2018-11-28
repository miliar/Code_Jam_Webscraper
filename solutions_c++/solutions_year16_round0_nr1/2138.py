#include<cstdio>
#include<cstring>
using namespace std;

bool f[20];

bool check(){
    bool t = true;
    for(int i = 0 ; i < 10 ; i++) t &= f[i];
    return t;
}

void add(int x){
    while(x){
        f[x%10] = true;
        x /= 10;
    }
}

int main(){
    int TN;
    scanf("%d", &TN);
    for(int casen = 1 ; casen <= TN ; casen++){
        printf("Case #%d: ", casen);
        memset(f, 0, sizeof(f));
        int n, cnt = 0;
        scanf("%d", &n);
        if(n == 0){
            puts("INSOMNIA");
            continue;
        }
        while(!check()){
            add (n * (++cnt));
        }
        printf("%d\n", n*cnt);
    }
    return 0;
}
