#include <cstdio>

using namespace std;

int solve(int n){
    if(n==0) return -1;
    int numbers[10];
    int s=0, c=0;
    for(int i=0;i<10;i++) numbers[i]=0;
    while(c<10){
        s++;
        int tmp = n*s;
        while(tmp>0){
            if(!numbers[tmp%10]){
                c++;
            }
            numbers[tmp%10]=1;
            tmp/=10;
        }
    }
    return n*s;
}

int main()
{
    int t,a;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        scanf("%d",&a);
        int tmp = solve(a);
        if(tmp<0) printf("Case #%d: INSOMNIA\n",i);
        else printf("Case #%d: %d\n",i,tmp);
    }
    return 0;
}
