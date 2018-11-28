#include<cstdio>
#include<cstring>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);

    int _, ca=1;
    scanf("%d", &_);
    while (_--)
    {
        int i ,n ;
        scanf("%d", &n);
        printf("Case #%d: ",ca++);
        if (n == 0)
        {
            printf("INSOMNIA\n");
            continue;
        }
        bool x[10];
        for(i = 0; i < 10 ; i++)
            x[i] = false;
        for(i = 1; ; i++)
        {
            int a = n * i ;
            while(a)
            {
                x[a%10] = true;
                a /= 10;
            }
            int j = 0;
            for(j = 0 ; j < 10 ; j++ )
            {
                if (x[j] == false)
                    break;
            }
            if (j == 10)
            {
                printf("%d\n", n * i );
                break;
            }
        }
    }
    return 0;
}
