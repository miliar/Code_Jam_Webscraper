#include <stdio.h>
#include <memory.h>

int n;

bool check[10];

void go_check(int num)
{
    while(num) {
        check[num%10]=true;
        num/=10;
    }
}

bool all_check()
{
    for(int i=0; i<10; i++) {
        if(!check[i]) return false;
    }
    return true;
}

void process()
{
    scanf("%d",&n);

    if(n==0) {
        printf("INSOMNIA\n");
        return;
    }

    memset(check,0,sizeof(check));
    for(int i=1;; i++){
        go_check(n*i);
        if(all_check()){
            printf("%d\n",n*i);
            break;
        }
    }
}

int main()
{
    freopen("A-large.in","rt",stdin);
    freopen("output.txt","wt",stdout);
    int t;
    scanf("%d",&t);
    for(int i=1; i<=t; i++) {
        printf("Case #%d: ",i);
        process();
    }
    return 0;
}
