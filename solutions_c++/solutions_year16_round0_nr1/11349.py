#include <cstdio>
int main()
{
    int t, n, s, r;
    scanf("%d",&t);
    for(int i = 1; i <= t; i++){
        scanf("%d",&n);
        if(n==0)
            printf("Case #%d: INSOMNIA\n",i);
        else {
            s = r = 0;
            while(r != 1023) {
                s += n;
                int x = s;
                while(x!=0){
                    r |= 1 << (x%10);
                    x /= 10;
                }
            }
            printf("Case #%d: %d\n", i, s);
        }
    }
}
