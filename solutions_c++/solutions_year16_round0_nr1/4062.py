#include<cstdio>
#include<cstdlib>
#include<cstring>

char num[1000000000+1];

int main()
{
    int T;
    scanf("%d", &T);
    for(int i=0; i<T; ++i)
    {
        int N;
        bool digit[10];
        for(int j=0; j<10; ++j) digit[j] = false;
        scanf("%s", num);
        N = atoi(num);
        if(N==0) printf("Case #%d: INSOMNIA\n", i+1);
        else
        {
            int now, true_num = 0;
            int round = 1;
            while(true_num!=10)
            {
                int l;
                now = round * N;
                sprintf(num, "%d", now);
                l = strlen(num);
                for(int j=0; j<l; ++j)
                {
                    if(!digit[num[j]-'0'])
                    {
                        digit[num[j]-'0'] = true;
                        true_num++;
                    }
                }
                round++;
            }
            printf("Case #%d: %d\n", i+1, now);
        }
    }
    return 0;
}
