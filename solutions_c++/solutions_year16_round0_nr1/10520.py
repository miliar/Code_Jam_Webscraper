#include<cstdio>

int fall_sleep(int num)
{
    bool check[10] = {0};
    int res = 0;
    while(true)
    {
        res += num;
        
        int temp = res;
        while(temp)
        {
            check[temp%10] = true;
            temp /= 10;
        }

        bool OK = true;
        for(int i=0; i<10; i++)
            if(!check[i])
            {
                OK = false;
                break;
            }
        if(OK)
            break;
    }
    return res;
}

int main(int argc, char* argv[])
{
    int T;
    scanf("%d", &T);

    for(int i=0; i<T; i++)
    {
        int num;
        scanf("%d", &num);
        if(num == 0)
            printf("Case #%d: INSOMNIA\n", i+1);
        else
            printf("Case #%d: %d\n", i+1, fall_sleep(num));
    }
    return 0;
}
