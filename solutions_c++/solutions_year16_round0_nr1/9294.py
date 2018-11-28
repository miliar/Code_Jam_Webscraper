#include <cstdio>
using namespace std;
int v [10];
void f(int k)
{
    int y;
    while(k>0)
    {
        y = k%10;
        k = k/10;
        v[y] = 1;
    }
}
int main()
{
    int m, n, i, j;
    scanf("%d", &m);
    for(i=0;i<m;i++)
    {
        int boo, insonia = -1, x = 1;
        long long int d0, d1;
        boo = 1;
        for(j=0;j<=9;j++)
            v[j] = -1;
        scanf("%lld", &d0);
        if(d0!=0){
        while(boo)
        {
            boo = 0;
            d1=d0*x;
            f(d1);
            for(j=0;j<=9;j++){
                if(v[j] != 1){
                    boo = 1;
                    x++;
                    break;
                }
            }
        }
        printf("Case #%d: %lld\n", i+1,d1);
        }
            else
                printf("Case #%d: INSOMNIA\n", i+1);
    }

    return 0;
}
