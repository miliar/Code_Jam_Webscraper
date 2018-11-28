#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

bool fg[10];

bool ok(){
    for(int i=0;i<10;i++)
        if(!fg[i]) return 0;
    return 1;
}

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("3.out", "w", stdout);
    int t,cas=1,n,i,j,tmp;
    scanf("%d", &t);
    while(t--){
        scanf("%d", &n);
        printf("Case #%d: ", cas++);
        if(n==0){
            printf("INSOMNIA\n");
            continue;
        }
        memset(fg, 0, sizeof(fg));
        for(i=1;;i++){
            tmp=n*i;
            while(tmp>=10){
                fg[tmp%10]=1;
                tmp/=10;
            }
            fg[tmp]=1;
            if(ok()) break;
        }
        printf("%d\n", n*i);
    }
    return 0;
}
