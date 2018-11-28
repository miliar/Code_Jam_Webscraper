#include <cstdio>
#include <cstdlib>

using namespace std;

int countSheep(int N);
int checkN(int flag[], int N);
int main()
{
    int T, cnt, N;

    scanf("%d", &T);
    cnt = 1;
    while(cnt <= T)
    {
        scanf("%d", &N);
        int result = countSheep(N);
        if(result == -1)
        {
            printf("Case #%d: INSOMNIA\n", cnt);
        }
        else
        {
            printf("Case #%d: %d\n", cnt, result);
        }
        cnt++;
    }
    return 0;
}

int countSheep(int N)
{
    int flag[11] = {0};
    for(int i=1; i<100; i++)
    {
        if(checkN(flag, N*i)==1)
        {
            return N*i;
        }
    }
    return -1;
}

int checkN(int flag[], int N)
{
    int tmp = N;
    while(tmp!=0)
    {
        flag[tmp%10] = 1;
        tmp = tmp/10;
    }
    for(int i=0; i<10; i++)
    {
        if(flag[i]==0)
        {
            return 0;
        }
    }
    return 1;
}
