#include<cstdio>
#include<cstring>
#include<cstdlib>
using namespace std;

int main()
{
    //freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);

    int _, ca=1, d=0,x,n;
    scanf("%d", &_);
    scanf("%d%d",&n,&x);
    while (_--)
    {
        char s[50] = "10000000000000000000000000000001";
        char s2[50] = "10000000000000000000000000000001";
        int step = 0 ;
        int dp[200];
        for(int i = 1 ; i < n-1 ; i ++)
            s[i] = '0';
        s[0] = '1';
        s[n-1] = '1';
        printf("Case #%d:\n",ca++);
        for(int i = 1; i < n-1 ; i ++)
        {
            strcpy(s2, s);
            s2[i]='1';
            for (int j = i + 1; j < n-1 ; j +=2)
            {
                s2[j] = '1';
                printf("%s 3 4 5 6 7 8 9 10 11\n", s2);
                x--;
                if ( x == 0)
                    break;
                s2[j] = '0';
            }
            if(x == 0)
                break;
        }
        for(int i = 1 ; i < n-1 ; i ++)
            s[i] = '0';
        s[0] = '1';
        s[1] = '1';
        s[2] = '1';
        s[n-1] = '1';
        for(int i = 3; i < n-1 ; i ++)
        {
            strcpy(s2, s);
            s2[i]='1';
            for (int j = i + 1; j < n-1 ; j +=2)
            {
                s2[j] = '1';
                printf("%s 3 4 5 6 7 8 9 10 11\n", s2);
                x--;
                if ( x == 0)
                    break;
                s2[j] = '0';
            }
            if(x == 0)
            break;
        }
        for(int i = 1 ; i < n-1 ; i ++)
            s[i] = '0';
        s[0] = '1';
        s[1] = '1';
        s[2] = '1';
        s[3] = '1';
        s[4] = '1';
        s[n-1] = '1';
        for(int i = 5; i < n-1 ; i ++)
        {
            strcpy(s2, s);
            s2[i]='1';
            for (int j = i + 1; j < n-1 ; j +=2)
            {
                s2[j] = '1';
                printf("%s 3 4 5 6 7 8 9 10 11\n", s2);
                x--;
                if ( x == 0)
                    break;
                s2[j] = '0';
            }
            if(x == 0)
            break;
        }
    }
    return 0;
}
